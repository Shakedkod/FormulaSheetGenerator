import re

from logic.diagram_utils import escape_latex, sanitize_id, layout_positions, edge_bend

_ATTR_RE = re.compile(r'(\w+)\s*=\s*("(?:[^"\\]|\\.)*"|[^,\]]+)')
_HEADER_RE = re.compile(r'^\s*(strict\s+)?(digraph|graph)\s+[A-Za-z0-9_"]*\s*\{', re.IGNORECASE)
_NODE_RE = re.compile(r'^"?(?P<id>[A-Za-z0-9_]+)"?\s*(\[(?P<attrs>.*)\])?$')
_EDGE_RE = re.compile(r'^"?(?P<src>[A-Za-z0-9_]+)"?\s*(?P<op>->|--)\s*"?(?P<dst>[A-Za-z0-9_]+)"?\s*(\[(?P<attrs>.*)\])?$')

_SHAPE_TIKZ_STYLE = {
    "box": "draw, rectangle",
    "rect": "draw, rectangle",
    "rectangle": "draw, rectangle",
    "circle": "draw, circle",
    "ellipse": "draw, ellipse",
    "oval": "draw, ellipse",
    "diamond": "draw, diamond, aspect=2",
}


def _parse_attrs(attr_str: str) -> dict:
    attrs = {}
    if not attr_str:
        return attrs
    for m in _ATTR_RE.finditer(attr_str):
        key = m.group(1).strip().lower()
        value = m.group(2).strip()
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        attrs[key] = value
    return attrs


def _strip_subgraphs(body: str) -> str:
    """
    Best-effort removal of (non-nested) subgraph blocks, so their internal
    rank/style statements don't get misread as top-level nodes or edges.
    Doesn't handle subgraphs nested inside subgraphs.
    """
    return re.sub(r'subgraph\s*[A-Za-z0-9_"]*\s*\{[^{}]*\}', "", body, flags=re.IGNORECASE)


def dot_to_tikz(code: str) -> str:
    """
    Best-effort conversion of a Graphviz DOT graph/digraph block into a
    TikZ picture. Supports node/edge statements with `label` and `shape`
    attributes, and the `rankdir` graph attribute.

    Layout is a generic automatic layered layout, not Graphviz's own
    layout engine, so it won't reproduce Graphviz's exact positioning, and
    nested subgraphs/clusters are stripped rather than rendered.

    Statements this parser doesn't recognize (graph-level attribute
    statements, `node`/`edge`/`graph` default blocks, etc.) are skipped
    rather than raising. Returns "" if no node/edge statement could be
    parsed at all, so the caller can fall back to a plain code listing.
    """
    header_match = _HEADER_RE.search(code)
    body = code[header_match.end():] if header_match else code
    body = body.rstrip()
    if body.endswith("}"):
        body = body[:-1]
    body = _strip_subgraphs(body)

    direction = "TB"
    nodes: dict[str, tuple[str, str]] = {}
    edges: list[tuple[str, str, str, str]] = []

    for raw_stmt in body.split(";"):
        stmt = re.sub(r"//.*", "", raw_stmt).strip()
        if not stmt:
            continue

        rankdir_m = re.match(r'^rankdir\s*=\s*"?(\w+)"?$', stmt, re.IGNORECASE)
        if rankdir_m:
            direction = rankdir_m.group(1).upper()
            continue
        if re.match(r"^(node|edge|graph)\s*\[", stmt, re.IGNORECASE):
            continue  # default-attribute statements aren't modeled

        m = _EDGE_RE.match(stmt)
        if m:
            src, dst = m.group("src"), m.group("dst")
            attrs = _parse_attrs(m.group("attrs"))
            nodes.setdefault(src, ("rectangle", src))
            nodes.setdefault(dst, ("rectangle", dst))
            edges.append((src, dst, attrs.get("label", ""), m.group("op")))
            continue

        m = _NODE_RE.match(stmt)
        if m:
            node_id = m.group("id")
            attrs = _parse_attrs(m.group("attrs"))
            shape = attrs.get("shape", "rectangle").lower()
            label = attrs.get("label", node_id)
            nodes[node_id] = (shape, label)
            continue
        # Unrecognized statement -- skip it rather than crash the build.

    if not nodes:
        return ""

    positions, layer = layout_positions(list(nodes.keys()), [(s, d) for s, d, _, _ in edges], direction)

    out = [
        r"\begin{LTR}",
        r"\begin{center}",
        r"\begin{tikzpicture}[",
        r"  every node/.style={draw, align=center, inner sep=4pt, minimum width=1.6cm, minimum height=0.9cm, font=\small},",
        r"  >={Stealth[length=3mm]}",
        r"]",
    ]
    for node_id, (shape, label) in nodes.items():
        x, y = positions[node_id]
        style = _SHAPE_TIKZ_STYLE.get(shape, "draw, rectangle")
        out.append(f"  \\node[{style}] ({sanitize_id(node_id)}) at ({x:.2f},{y:.2f}) {{{escape_latex(label)}}};")
    for src, dst, label, op in edges:
        arrow = "->" if op == "->" else "-"
        label_part = f" node[midway, fill=white, font=\\scriptsize] {{{escape_latex(label)}}}" if label else ""
        bend = edge_bend(src, dst, layer, direction)
        connector = f"to[{bend}]" if bend else "--"
        out.append(f"  \\draw[{arrow}] ({sanitize_id(src)}) {connector}{label_part} ({sanitize_id(dst)});")
    out += [r"\end{tikzpicture}", r"\end{center}", r"\end{LTR}"]
    return "\n".join(out) + "\n"
