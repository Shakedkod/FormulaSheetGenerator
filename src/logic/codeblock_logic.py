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

def codeblock(block: dict, head: dict) -> tuple[str, dict]:
    """
    Converts a code block AST node to LaTeX content.
    """
    head["code"] = True
    block_type = block.get("attrs", {}).get("info", "")
    
    match block_type:
        case "mermaid":
            head["tikz"] = True
            pass
            #return mermaid(block.get("raw", ""))
        case "dot":
            head["tikz"] = True
            pass
            #return dot(block.get("raw", ""))
        case "desmos-graph":
            head["tikz"] = True
            # return desmos_graph(block.get("raw", ""))
            return (generic_codeblock(block.get("raw", ""), "text"), head)
        case _:
            return (generic_codeblock(block.get("raw", ""), block_type), head)