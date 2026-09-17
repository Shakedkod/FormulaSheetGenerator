from rich.console import Console
from logic.latex_parts import get_text, get_header, blank_line, math_block, parse_list, table, thematic_break
from logic.obsidian_special_blocks import quote, callout
from logic.codeblock_logic import codeblock

console = Console()

def parse_ast_to_latex(ast: dict, head: dict = None) -> tuple[str, dict]:
    """
    Parses the abstract syntax tree (AST) to a LaTeX document.
    """
    new_head = head.copy() if head else {}

    # Convert the AST to LaTeX content
    latex_content, new_head = ast_to_latex(ast, head)

    return (latex_content, new_head)

def ast_to_latex(ast: dict, head: dict) -> tuple[str, dict]:
    """
    Converts the abstract syntax tree (AST) to LaTeX content.
    """
    # This function should be implemented to convert the AST to LaTeX.
    # For now, it returns an empty string.
    result = ""
    
    for node in ast:
        if node["type"] == "heading":
            result += get_header(node)
        elif node["type"] == "paragraph":
            result_temp, head = get_text(node.get("children", []), head)
            result += result_temp + blank_line()
        elif node["type"] == "table":
            result += table(node) + blank_line()
        elif node["type"] == "list":
            result += parse_list(node) + blank_line()
        elif node["type"] == "blank_line":
            result += blank_line()
        elif node["type"] == "thematic_break":
            result += thematic_break()
        elif node["type"] == "block_code":
            result_temp, head = codeblock(node, head)
            result += result_temp
        elif node["type"] == "block_quote":
            result_temp, head = ast_to_latex(node.get("children", []), head)
            result += quote(result_temp, "quote")
        elif node["type"] == "callout":
            result_temp, head = ast_to_latex(node.get("children", []), head)
            attrs: dict = node.get("attrs", {})
            result += callout(result_temp, attrs)
        elif node["type"] == "proof":
            result_temp, head = ast_to_latex(node.get("children", []), head)
            result += "\\begin{proof}\n" + result_temp + "\n\\end{proof}\n"
        elif node["type"] == "block_math":
            result += math_block(node.get("raw", "")) + blank_line()
        else:
            console.print(f"[yellow]Warning: Unhandled AST node type: {node['type']}[/yellow]")

    
    return (result, head)

def second_pass_parse(latex_content: str) -> str:
    """
    Performs a second pass on the LaTeX content to handle any additional processing.
    """
    
    # check for unfound $$\n {math} \n$$ and replace them with \[ {math} \]
    import re
    pattern = r"\$\$\n(.*?)\n\$\$"
    latex_content = re.sub(pattern, r"\\[\1\\]", latex_content, flags=re.DOTALL)
    
    # check for unfound $ {math} $ and replace them with \( {math} \)
    pattern = r"\$(.*?)\$"
    latex_content = re.sub(pattern, r"\\(\1\\)", latex_content, flags=re.DOTALL)

    return latex_content