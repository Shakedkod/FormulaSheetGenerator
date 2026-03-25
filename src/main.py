import os, sys

from rich.console import Console
import mistune

from logic.latex import BASE_LATEX_DOC_END, BASE_LATEX_DOC_START, BASE_LATEX_DOC_START_DOC, LATEX_HEBREW_MODIFIER, generate_latex_from_node

console = Console()

# Creates an abstract syntax tree (AST) renderer
markdown_parser = mistune.create_markdown(renderer=None, plugins=['strikethrough', 'table', 'task_lists', 'footnotes', 'def_list', 'math', "url"], hard_wrap=True)

def main():
    ast: list = None
    try:
        with open(".\\test\\sample_he.md", "r", encoding="utf-8") as f:
            text = f.read()
            ast = markdown_parser(text)
    except Exception as e:
        console.print(f"[red]Error reading markdown file: {e}[/red]")
        exit(1)

    # Parsing the AST to a latex document.
    # Start the document
    column_num = 3
    if ("--column-num" in sys.argv):
        try:
            column_num_index = sys.argv.index("--column-num") + 1
            if (column_num_index < len(sys.argv)):
                column_num = int(sys.argv[column_num_index])
            else:
                console.print("[yellow]Warning: --column-num flag provided without a number, using default of 3 columns[/yellow]")
        except ValueError:
            console.print("[yellow]Warning: Invalid number provided for --column-num, using default of 3 columns[/yellow]")
    
    if (len(sys.argv) > 1 and sys.argv[1] == "--he"):
        final_document: str = BASE_LATEX_DOC_START + LATEX_HEBREW_MODIFIER + BASE_LATEX_DOC_START_DOC + f"{{{column_num}}}" + "\n"
    else:
        final_document: str = BASE_LATEX_DOC_START + BASE_LATEX_DOC_START_DOC + f"{{{column_num}}}" + "\n"
    section_num = 0
    
    # document content
    for node in ast:
        output = generate_latex_from_node(node, section_num)
        if (output is not None):
            final_document += output[0] + output[2] + "\n"
            section_num += output[1]
        else:
            console.print(f"[yellow]Warning: Unsupported node type '{node['type']}'[/yellow]")
    
    # End the document
    final_document += "\n" + BASE_LATEX_DOC_END
    
    with open(".\\test\\output.tex", "w", encoding="utf-8") as f:
        f.write(final_document)
    
    # Compile the LaTeX document to PDF
    try:
        os.system("xelatex test\\output.tex")
    except Exception as e:
        console.print(f"[red]Error compiling LaTeX document: {e}[/red]")


if __name__ == "__main__":
    main()