import re
from collections import defaultdict, deque

_LATEX_ESCAPES = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}


def escape_latex(text: str) -> str:
    """
    Escapes LaTeX special characters in a plain-text label pulled out of a
    diagram source (mermaid/dot labels are not LaTeX, so anything in them
    needs escaping before it lands in a \\node{...}).
    """
    if not text:
        return ""
    return "".join(_LATEX_ESCAPES.get(ch, ch) for ch in text)


def sanitize_id(node_id: str) -> str:
    """
    Turns an arbitrary diagram node id into a valid TikZ node name
    (letters/digits only, never starting with a digit).
    """
    safe = re.sub(r"[^A-Za-z0-9]", "_", node_id)
    if not safe or safe[0].isdigit():
        safe = "n" + safe
    return safe


def compute_layers(node_ids, edges) -> dict:
    """
    Assigns each node a layer (0-based) using longest-path-from-root
    layering. Nodes only reachable through a cycle (so never topologically
    resolved) are placed one layer after everything that could be ordered,
    so the layout always completes even on graphs that aren't strict DAGs.
    """
    node_set = set(node_ids)
    outgoing = defaultdict(list)
    indeg = {n: 0 for n in node_ids}
    for src, dst in edges:
        if src in node_set and dst in node_set:
            outgoing[src].append(dst)
            indeg[dst] += 1

    layer = {n: 0 for n in node_ids}
    indeg_work = dict(indeg)
    queue = deque([n for n in node_ids if indeg_work[n] == 0])
    visited = set(queue)

    while queue:
        n = queue.popleft()
        for m in outgoing.get(n, []):
            layer[m] = max(layer[m], layer[n] + 1)
            indeg_work[m] -= 1
            if indeg_work[m] == 0 and m not in visited:
                visited.add(m)
                queue.append(m)

    leftover = [n for n in node_ids if n not in visited]
    if leftover:
        next_layer = (max(layer.values()) + 1) if layer else 0
        for n in leftover:
            layer[n] = next_layer

    return layer


def layout_positions(node_ids, edges, direction: str = "TB", layer_gap: float = 3.8, node_gap: float = 2.4):
    """
    Produces {node_id: (x, y)} coordinates (in cm) for a simple layered
    graph layout, plus the {node_id: layer} map used to compute them.
    `direction` is one of TB/TD, BT, LR, RL (mermaid/dot style). This is a
    generic auto-layout, not a reimplementation of mermaid's or Graphviz's
    own layout engine, so it won't reproduce their exact positioning -- it
    just guarantees something legible and non-overlapping.
    """
    layer = compute_layers(node_ids, edges)
    layers = defaultdict(list)
    for n in node_ids:
        layers[layer[n]].append(n)

    positions = {}
    for lvl, nodes_in_layer in layers.items():
        count = len(nodes_in_layer)
        offset = (count - 1) / 2.0
        for i, n in enumerate(nodes_in_layer):
            cross = (i - offset) * node_gap
            along = lvl * layer_gap
            if direction == "LR":
                positions[n] = (along, -cross)
            elif direction == "RL":
                positions[n] = (-along, -cross)
            elif direction == "BT":
                positions[n] = (cross, along)
            else:  # TB / TD
                positions[n] = (cross, -along)
    return positions, layer


_BEND_ANGLES = {
    "TB": ("-60", "60"),
    "BT": ("60", "-60"),
    "LR": ("-150", "-30"),
    "RL": ("-30", "-150"),
}


def edge_bend(src: str, dst: str, layer: dict, direction: str = "TB") -> str:
    """
    Returns a TikZ `to[out=..., in=...]` bend option for edges that skip
    more than one layer (e.g. a decision node with a branch that
    reconverges further down). Without this, a skip-edge is a straight
    line whose midpoint can land exactly on top of an intermediate node --
    and an edge label drawn there will paint right over that node, hiding
    it completely. The bend angles are chosen perpendicular to the main
    flow direction so the curve swings clear of the straight-line column.
    A non-skip edge (adjacent layers) returns "" so a plain `--`
    connector is used.
    """
    if abs(layer.get(dst, 0) - layer.get(src, 0)) > 1:
        out_angle, in_angle = _BEND_ANGLES.get(direction, _BEND_ANGLES["TB"])
        return f"out={out_angle}, in={in_angle}"
    return ""
