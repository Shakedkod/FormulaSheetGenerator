def desmos_graph(code: str) -> str:
    """
    Converts a Desmos graph code block to LaTeX tikz picture.
    """
    info, *body = code.split("\n---\n", 1)
    info_dicts = [dict(item.split("=") for item in line.split(";")) for line in info.splitlines()]


def generic_codeblock(code: str, language: str) -> str:
    """
    Converts a generic code block to LaTeX content.
    """
    if not language or language == "text":
        return f"\\begin{{LTR}}\\begin{{lstlisting}}\n{code}\n\\end{{lstlisting}}\\end{{LTR}}"
    return f"\\begin{{LTR}}\\begin{{lstlisting}}[language={language}]\n{code}\n\\end{{lstlisting}}\\end{{LTR}}"

def codeblock(block: dict) -> str:
    """
    Converts a code block AST node to LaTeX content.
    """
    block_type = block.get("attrs", {}).get("info", "")
    
    match block_type:
        case "mermaid":
            pass
            #return mermaid(block.get("raw", ""))
        case "dot":
            pass
            #return dot(block.get("raw", ""))
        case "desmos-graph":
            # return desmos_graph(block.get("raw", ""))
            return generic_codeblock(block.get("raw", ""), "text")
        case _:
            return generic_codeblock(block.get("raw", ""), block_type)