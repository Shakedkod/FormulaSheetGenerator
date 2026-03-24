import json
import os

from rich.console import Console
import mistune

from src.logic.latex import BASE_LATEX_DOC_END, BASE_LATEX_DOC_START, generate_latex_from_node

console = Console()

# Creates an abstract syntax tree (AST) renderer
markdown_parser = mistune.create_markdown(renderer=None, plugins=['strikethrough', 'table', 'task_lists', 'footnotes', 'def_list', 'math', "url"], hard_wrap=True)

def main():
    ast: list = None
    try:
        with open(".\\test\\sample_he.md", "r", encoding="utf-8") as f:
            text = f.read()
            ast = markdown_parser(text)
            with open(".\\test\\ast.json", "w", encoding="utf-8") as f:
                json.dump(ast, f, indent=4, ensure_ascii=False)
    except Exception as e:
        console.print(f"[red]Error reading markdown file: {e}[/red]")
        exit(1)

    # Parsing the AST to a latex document.
    # Start the document
    final_document: str = BASE_LATEX_DOC_START + "\n"
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