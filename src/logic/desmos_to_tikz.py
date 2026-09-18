import re

_KV_RE = re.compile(r"^\s*([A-Za-z]+)\s*=\s*(.+?)\s*$")
_FUNC_LINE_RE = re.compile(r"^\s*\w+\s*\(\s*x\s*\)\s*=\s*(.+?)\s*$")
_RANGE_RE = re.compile(r"^\s*(-?[\d.]+)\s*(<=|<)\s*x\s*(<=|<)\s*(-?[\d.]+)\s*$")
_UPPER_RE = re.compile(r"^\s*x\s*(<=|<)\s*(-?[\d.]+)\s*$")
_LOWER_RE = re.compile(r"^\s*x\s*(>=|>)\s*(-?[\d.]+)\s*$")


def _parse_config(info_text: str) -> dict:
    """
    Parses the `key=value; key2=value2` header lines used by this
    project's desmos-graph fences (e.g. `width=200; height=200;` /
    `bottom=-1; top=2`) into a single merged dict.
    """
    config = {}
    for raw_line in info_text.splitlines():
        for item in raw_line.split(";"):
            item = item.strip()
            if not item:
                continue
            m = _KV_RE.match(item)
            if m:
                config[m.group(1).lower()] = m.group(2)
    return config


def _num(config: dict, key: str, default: float) -> float:
    try:
        return float(config[key])
    except (KeyError, ValueError):
        return default


def _parse_domain(condition: str, left: float, right: float) -> tuple[float, float]:
    """
    Converts a desmos-style domain condition (`x<0`, `x>=1`, `-2<x<3`) into
    a (min, max) pair for pgfplots' `domain=min:max`. Falls back to the
    full viewport width when there's no condition, or one we don't
    recognize.
    """
    condition = condition.strip()
    if not condition:
        return (left, right)
    m = _RANGE_RE.match(condition)
    if m:
        return (float(m.group(1)), float(m.group(4)))
    m = _UPPER_RE.match(condition)
    if m:
        return (left, float(m.group(2)))
    m = _LOWER_RE.match(condition)
    if m:
        return (float(m.group(2)), right)
    return (left, right)


def _expr_to_pgfmath(expr: str) -> str:
    """
    Small best-effort cleanup: Desmos allows implicit multiplication (e.g.
    `2x`, `3(x+1)`) which pgfmath (the default pgfplots math engine) does
    not, so we insert the `*`. More advanced Desmos syntax (fractions,
    absolute-value bars, piecewise braces, etc.) is not converted and will
    need manual adjustment after generation.
    """
    expr = expr.strip()
    expr = re.sub(r"(\d)\s*([a-zA-Z(])", r"\1*\2", expr)
    expr = re.sub(r"(\))\s*([a-zA-Z0-9(])", r"\1*\2", expr)
    return expr


def desmos_graph_to_tikz(code: str) -> str:
    """
    Best-effort conversion of this project's custom `desmos-graph` code
    fence into a pgfplots axis. Expected format (as used in the test
    notes):

        width=200; height=200;
        bottom=-1; top=2
        ---
        f(x)=0 |x<0
        g(x)=1 |x>1

    A header of `key=value;` pairs (width/height/left/right/bottom/top),
    a `---` separator, then one `name(x)=expr [|domain condition]` line
    per function to plot. `left`/`right` default to `bottom`/`top` when
    omitted, matching the square-viewport examples in this repo's test
    files -- adjust the header if you actually want an asymmetric x-range.

    Requires the `pgfplots` package; the caller is responsible for
    enabling it in the document head (see the `pgfplots` head flag).

    Returns "" if no function line could be parsed, so the caller can fall
    back to a plain code listing instead of emitting an empty plot.
    """
    parts = re.split(r"\n?-{3,}\n?", code, maxsplit=1)
    info_text = parts[0] if parts else ""
    body_text = parts[1] if len(parts) > 1 else ""

    config = _parse_config(info_text)
    bottom = _num(config, "bottom", -5.0)
    top = _num(config, "top", 5.0)
    left = _num(config, "left", -5.0)
    right = _num(config, "right", 5.0)
    width_px = _num(config, "width", 400.0)
    height_px = _num(config, "height", 400.0)

    aspect = (width_px / height_px) if height_px else 1.0
    plot_height_cm = 6.0
    plot_width_cm = plot_height_cm * aspect

    functions = []
    for raw_line in body_text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        expr_part, _, domain_part = line.partition("|")
        m = _FUNC_LINE_RE.match(expr_part)
        if not m:
            continue
        expr = _expr_to_pgfmath(m.group(1))
        domain = _parse_domain(domain_part, left, right)
        functions.append((expr, domain))

    if not functions:
        return ""

    out = [
        r"\begin{LTR}",
        r"\begin{center}",
        r"\begin{tikzpicture}",
        rf"\begin{{axis}}[width={plot_width_cm:.2f}cm, height={plot_height_cm:.2f}cm, "
        rf"xmin={left:g}, xmax={right:g}, ymin={bottom:g}, ymax={top:g}, "
        r"axis lines=middle, samples=200, thick, "
        r"xlabel={$x$}, ylabel={$y$}]",
    ]
    for expr, (dmin, dmax) in functions:
        out.append(rf"\addplot[domain={dmin:g}:{dmax:g}] {{{expr}}};")
    out += [r"\end{axis}", r"\end{tikzpicture}", r"\end{center}", r"\end{LTR}"]
    return "\n".join(out) + "\n"
