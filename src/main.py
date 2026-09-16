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

PREAMBLE_FLAGS = ("--preamble", "-p")
STYLE_FLAGS = ("--style", "-s")
STYLES = ("regular", "fancy-academic")

def check_flag(location: int, argv: list[str], flags: tuple, command: callable) -> bool:
    if argv[location] in flags:
        if len(argv) < location + 2:
            console.print(f"[red]Error: No argument specified for flag '{argv[location]}'.[/red]")
            return False
        if not command(argv[location + 1]):
            console.print(f"[red]Error: Invalid argument '{argv[location + 1]}' for flag '{argv[location]}'.[/red]")
            return False
    return True

def test_args(argv: list[str]) -> bool:
    """
    Tests the command line arguments.
    """
    if len(argv) < 2:
        console.print("[red]Error: No input file specified.[/red]")
        return False
    if not os.path.isfile(argv[1]):
        console.print(f"[red]Error: Input file '{argv[1]}' does not exist.[/red]")
        return False
    if len(argv) > 2:
        preamble_flag_count = sum(1 for arg in argv[2:] if arg in PREAMBLE_FLAGS)
        style_flag_count = sum(1 for arg in argv[2:] if arg in STYLE_FLAGS)
        if preamble_flag_count > 1:
            console.print("[red]Error: Multiple preamble flags specified.[/red]")
            return False
        if style_flag_count > 1:
            console.print("[red]Error: Multiple style flags specified.[/red]")
            return False
        
        if not (check_flag(2, argv, PREAMBLE_FLAGS, os.path.isfile) and check_flag(2, argv, STYLE_FLAGS, lambda x: x in STYLES) and check_flag(2, argv, ("--no-toc", "-nt"), lambda x: True)):
            return False
        
        if len(argv) > 4:
            if not (check_flag(4, argv, PREAMBLE_FLAGS, os.path.isfile) and check_flag(4, argv, STYLE_FLAGS, lambda x: x in STYLES) and check_flag(4, argv, ("--no-toc", "-nt"), lambda x: True)):
                return False
            
            if len(argv) > 6:
                if not (check_flag(6, argv, PREAMBLE_FLAGS, os.path.isfile) and check_flag(6, argv, STYLE_FLAGS, lambda x: x in STYLES) and check_flag(6, argv, ("--no-toc", "-nt"), lambda x: True)):
                    return False
                
                if len(argv) > 8:
                    console.print("[red]Error: Too many arguments specified.[/red]")
                    return False
    return True

def get_argument_value(argv: list[str], flags: tuple, default: str) -> str:
    """
    Gets the value of the argument specified by the flags.
    """
    for i in range(2, len(argv), 2):
        if argv[i] in flags:
            return argv[i + 1]
    return default

def main(input: str, preamble: str = None, style: str = "regular"):
    ast = None
    isPreamble = False
    preamble_text = ""
    try:
        with open(".\\test\\UniTest4.md", "r", encoding="utf-8") as f:
            text = f.read()
            ast = markdown_parser(text)
    except Exception as e:
        console.print(f"[red]Error reading markdown file: {e}[/red]")
        sys.exit(1)
    
    try:
        with open(".\\test\\preamble.sty", "r", encoding="utf-8") as f:
            preamble_text = f.read()
            isPreamble = True
    except Exception as e:
        console.print(f"[red]Error reading preamble file: {e}[/red]")
        sys.exit(1)

    # Parsing the AST to a latex document.
    ast = remove_metadata(ast)
    latex_content = "\\title{Sample Document}\n\\author{test}\n" + parse_ast_to_latex(ast, preamble_text if isPreamble else "")
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
    if test_args(sys.argv):
        input_file = sys.argv[1]
        preamble_file = None
        style = "regular"

        if len(sys.argv) > 2:
            preamble_file = get_argument_value(sys.argv, PREAMBLE_FLAGS, None)
            style = get_argument_value(sys.argv, STYLE_FLAGS, "regular")
        
        main(input_file, preamble_file, style)
    else:
        console.print("[blue]Usage: python main.py <input_file> [--preamble|-p <preamble_file>] [--style|-s <regular|fancy-academic>] [--no-toc|-nt][/blue]")
        sys.exit(1)
