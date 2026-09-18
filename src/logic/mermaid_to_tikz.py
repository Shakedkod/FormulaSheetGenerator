import re

from logic.diagram_utils import escape_latex, sanitize_id, layout_positions, edge_bend

_DIRECTION_RE = re.compile(r"^\s*(?:graph|flowchart)\s+(TB|TD|BT|RL|LR)\b", re.IGNORECASE)

_SHAPE_PATTERNS = [
    (re.compile(r"^\[\[(.*)\]\]$", re.DOTALL), "subroutine"),
    (re.compile(r"^\[\((.*)\)\]$", re.DOTALL), "cylinder"),
    (re.compile(r"^\(\((.*)\)\)$", re.DOTALL), "circle"),
    (re.compile(r"^\{(.*)\}$", re.DOTALL), "diamond"),
    (re.compile(r"^\((.*)\)$", re.DOTALL), "rounded"),
    (re.compile(r"^\[(.*)\]$", re.DOTALL), "rectangle"),
    (re.compile(r"^>(.*)\]$", re.DOTALL), "flag"),
]

_SHAPE_TIKZ_STYLE = {
    "rectangle": "draw, rectangle",
    "rounded": "draw, rectangle, rounded corners",
    "circle": "draw, circle",
    "diamond": "draw, diamond, aspect=2",
    "subroutine": "draw, rectangle, double",
    "cylinder": "draw, cylinder, shape border rotate=90",
    "flag": "draw, rectangle",
}

_NODE_TOKEN = r"[A-Za-z0-9_.-]+"
_SHAPE_TOKEN = r"(?:\[\[.*?\]\]|\[\(.*?\)\]|\(\(.*?\)\)|\{.*?\}|\(.*?\)|\[.*?\]|>[^\]]*\])"
_ARROW_TOKEN = r"(?:-\.{1,2}->|={1,3}>|-{1,3}>|-\.{1,2}-|={2,3}|-{2,3})"

_EDGE_RE = re.compile(
    rf"^\s*(?P<src>{_NODE_TOKEN})\s*(?P<src_shape>{_SHAPE_TOKEN})?"
    rf"\s*(?P<arrow>{_ARROW_TOKEN})\s*(?:\|(?P<label>[^|]*)\|)?\s*"
    rf"(?P<dst>{_NODE_TOKEN})\s*(?P<dst_shape>{_SHAPE_TOKEN})?\s*$"
)
_NODE_ONLY_RE = re.compile(rf"^\s*(?P<id>{_NODE_TOKEN})\s*(?P<shape>{_SHAPE_TOKEN})?\s*$")

_SKIP_PREFIXES = ("subgraph", "end", "classDef", "class ", "click ", "style ", "linkStyle", "%%")


def _parse_shape(shape_token: str, node_id: str) -> tuple[str, str]:
    """
    Returns (shape_name, label) for a raw mermaid shape token like '[Text]'.
    Falls back to a plain rectangle labeled with the node id when there's
    no shape token at all (e.g. the node was only ever mentioned in an
    edge).
    """
    if not shape_token:
        return ("rectangle", node_id)
    for pattern, shape_name in _SHAPE_PATTERNS:
        m = pattern.match(shape_token)
        if m:
            return (shape_name, m.group(1).strip())
    return ("rectangle", shape_token.strip("[](){}"))


def mermaid_to_tikz(code: str) -> str:
    """
    Best-effort conversion of a mermaid flowchart/graph block into a TikZ
    picture. Supports the common node shapes ([], (), (()), {}, [[]], [()])
    and edge styles (-->, ---, -.->, -.-, ==>, ===), plus |label| edge text.

    Layout is a generic automatic layered layout, not mermaid's own layout
    engine, so it won't match mermaid's rendering pixel-for-pixel -- it
    just guarantees a readable, non-overlapping diagram.

    Lines this parser doesn't recognize (chained edges on one line like
    `A --> B --> C`, subgraphs, styling directives, etc.) are skipped
    rather than raising, so an unusual diagram degrades gracefully instead
    of crashing the whole document build. Returns "" if nothing could be
    parsed at all, so the caller can fall back to a plain code listing.
    """
    lines = code.splitlines()
    direction = "TB"

    body_lines = lines
    if lines:
        m = _DIRECTION_RE.match(lines[0])
        if m:
            direction = m.group(1).upper()
            if direction == "TD":
                direction = "TB"
            body_lines = lines[1:]

    nodes: dict[str, tuple[str, str]] = {}
    edges: list[tuple[str, str, str]] = []

    def register(node_id: str, shape_token: str = ""):
        if node_id not in nodes or shape_token:
            nodes[node_id] = _parse_shape(shape_token, node_id)

    for raw_line in body_lines:
        line = raw_line.split("%%", 1)[0].strip()
        if not line or line in ("{", "}") or line.startswith(_SKIP_PREFIXES):
            continue

        m = _EDGE_RE.match(line)
        if m:
            src, dst = m.group("src"), m.group("dst")
            register(src, m.group("src_shape") or "")
            register(dst, m.group("dst_shape") or "")
            edges.append((src, dst, (m.group("label") or "").strip()))
            continue

        m = _NODE_ONLY_RE.match(line)
        if m:
            register(m.group("id"), m.group("shape") or "")
            continue
        # Unrecognized line -- skip it rather than crash the build.

    if not nodes:
        return ""

    positions, layer = layout_positions(list(nodes.keys()), [(s, d) for s, d, _ in edges], direction)

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
    for src, dst, label in edges:
        label_part = f" node[midway, fill=white, font=\\scriptsize] {{{escape_latex(label)}}}" if label else ""
        bend = edge_bend(src, dst, layer, direction)
        connector = f"to[{bend}]" if bend else "--"
        out.append(f"  \\draw[->] ({sanitize_id(src)}) {connector}{label_part} ({sanitize_id(dst)});")
    out += [r"\end{tikzpicture}", r"\end{center}", r"\end{LTR}"]
    return "\n".join(out) + "\n"
