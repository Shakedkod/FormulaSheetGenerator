import os, sys

from rich.console import Console

from logic.obs_markdown_extras import markdown_parser
from logic.ast_to_latex import parse_ast_to_latex, second_pass_parse

console = Console()

def remove_metadata(ast):
    """
    Removes the metadata from the AST.
    """
    if ast[0]["type"] == "thematic_break":
        ast = ast[1:]
        ast = ast[ast.index(next(x for x in ast if x["type"] == "thematic_break")) + 1:]
    return ast

def main():
    ast = None
    isPreamble = False
    preamble = ""
    try:
        with open(".\\test\\UniTest4.md", "r", encoding="utf-8") as f:
            text = f.read()
            ast = markdown_parser(text)
    except Exception as e:
        console.print(f"[red]Error reading markdown file: {e}[/red]")
        sys.exit(1)
    
    try:
        with open(".\\test\\preamble.sty", "r", encoding="utf-8") as f:
            preamble = f.read()
            isPreamble = True
    except Exception as e:
        console.print(f"[red]Error reading preamble file: {e}[/red]")
        sys.exit(1)

    # Parsing the AST to a latex document.
    ast = remove_metadata(ast)
    latex_content = "\\title{Sample Document}\n\\author{test}\n" + parse_ast_to_latex(ast, preamble if isPreamble else "")
    latex_content = second_pass_parse(latex_content)

    with open(".\\test\\ast.json", "w", encoding="utf-8") as f:
        import json
        json.dump(ast, f, ensure_ascii=False, indent=4)
    with open(".\\test\\output.tex", "w", encoding="utf-8") as f:
        f.write(latex_content)

    # Compile the LaTeX document to PDF
    try:
        os.system("xelatex test\\output.tex")
    except Exception as e:
        console.print(f"[red]Error compiling LaTeX document: {e}[/red]")


if __name__ == "__main__":
    main()
