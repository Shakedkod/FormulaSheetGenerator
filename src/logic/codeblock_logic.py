from logic.desmos_to_tikz import desmos_graph_to_tikz
from logic.dot_to_tikz import dot_to_tikz
from logic.mermaid_to_tikz import mermaid_to_tikz


def generic_codeblock(code: str, language: str) -> str:
    """
    Converts a generic code block to LaTeX content.
    """
    if not language or language == "text":
        return f"\\begin{{LTR}}\\begin{{lstlisting}}\n{code}\n\\end{{lstlisting}}\\end{{LTR}}"
    return f"\\begin{{LTR}}\\begin{{lstlisting}}[language={language}]\n{code}\n\\end{{lstlisting}}\\end{{LTR}}"

def codeblock(block: dict, head: dict) -> tuple[str, dict]:
    """
    Converts a code block AST node to LaTeX content.
    """
    head["code"] = True
    block_type = block.get("attrs", {}).get("info", "")
    
    match block_type:
        case "mermaid":
            head["tikz"] = True
            tikz = mermaid_to_tikz(block.get("raw", ""))
            return (tikz or generic_codeblock(block.get("raw", ""), "text"), head)
        case "dot":
            head["tikz"] = True
            tikz = dot_to_tikz(block.get("raw", ""))
            return (tikz or generic_codeblock(block.get("raw", ""), "text"), head)
        case "desmos-graph":
            head["tikz"] = True
            head["packages"].append("pgfplots")
            tikz = desmos_graph_to_tikz(block.get("raw", ""))
            return (tikz or generic_codeblock(block.get("raw", ""), "text"), head)
        case _:
            return (generic_codeblock(block.get("raw", ""), block_type), head)