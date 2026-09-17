import os, sys
import questionary
from questionary import Style

from rich.console import Console

from logic.obs_markdown_extras import markdown_parser
from logic import LatexFile

console = Console()

def remove_metadata(ast):
    """
    Removes the metadata from the AST.
    """
    if ast[0]["type"] == "thematic_break":
        ast = ast[1:]
        ast = ast[ast.index(next(x for x in ast if x["type"] == "thematic_break")) + 1:]
    return ast

# Custom style to match that create-next-app teal/purple look
custom_style = Style([
    ("qmark", "fg:#00d7af bold"),        # the ? at the start
    ("question", "bold"),
    ("answer", "fg:#00d7af bold"),       # the answer once selected
    ("pointer", "fg:#00d7af bold"),      # the arrow pointer
    ("highlighted", "fg:#00d7af bold"),  # highlighted choice
    ("selected", "fg:#00d7af"),
    ("separator", "fg:#6C6C6C"),
    ("instruction", "fg:#6C6C6C italic"),
])


def run_wizard():
    print()  # spacing like create-next-app's initial banner
    questionary.print("📄  Markdown To LaTeX", style="bold fg:#00d7af")
    print()

    input_file = questionary.path(
        "What input file would you like to use?",
        style=custom_style,
    ).ask()
    if input_file is None:
        sys.exit(0)  # Ctrl+C

    style = questionary.select(
        "Which style would you like to use?",
        choices=["regular", "fancy-academic"],
        style=custom_style,
    ).ask()

    use_preamble = questionary.confirm(
        "Include a custom preamble file?", default=False, style=custom_style
    ).ask()
    preamble = None
    if use_preamble:
        preamble = questionary.path("Path to preamble file:", style=custom_style).ask()

    toc = questionary.confirm(
        "Include a table of contents?", default=True, style=custom_style
    ).ask()

    title = questionary.text("Document title:", style=custom_style).ask()
    author = questionary.text("Author name:", style=custom_style).ask()

    hide_date = questionary.confirm(
        "Hide the date?", default=False, style=custom_style
    ).ask()
    date = None
    if not hide_date:
        date = questionary.text(
            "Date (leave blank for today):", style=custom_style
        ).ask()

    header = questionary.text(
        "Header text (leave blank for none):", style=custom_style
    ).ask()
    footer = questionary.text(
        "Footer text (leave blank for page number):", style=custom_style
    ).ask()

    language = questionary.select(
        "Document language?",
        choices=["english", "hebrew", "other"],
        style=custom_style,
    ).ask()
    if language == "other":
        language = questionary.text("Enter language code:", style=custom_style).ask()

    print()
    questionary.print("✔ ", style="bold fg:#00d7af", end="")
    questionary.print("Configuration complete!\n", style="bold")

    return {
        "input_file": input_file,
        "preamble": preamble,
        "style": style,
        "toc": toc,
        "title": title or None,
        "author": author or None,
        "date": date or None,
        "footer": footer or None,
        "header": header or None,
        "language": language,
        "hide_date": hide_date,
    }

def main():
    ast = None
    isPreamble = False
    preamble_text = ""
    args = run_wizard()
    
    try:
        with open(args["input_file"], "r", encoding="utf-8") as f:
            text = f.read()
            ast = markdown_parser(text)
    except Exception as e:
        console.print(f"[red]Error reading markdown file: {e}[/red]")
        sys.exit(1)
    
    try:
        with open(args["preamble"], "r", encoding="utf-8") as f:
            preamble_text = f.read()
            isPreamble = True
    except Exception as e:
        console.print(f"[red]Error reading preamble file: {e}[/red]")
        sys.exit(1)

    # Parsing the AST to a latex document.
    ast = remove_metadata(ast)
    latex_file = LatexFile(
        preamble=preamble_text,
        theme=args["style"],
        language=args["language"],
        author=args["author"] or "",
        title=args["title"] or "",
        doc_date=args["date"] or "",
        toc=args["toc"]
    )
    latex_file.md_to_latex(ast)

    with open(args["input_file"].replace(".md", ".tex"), "w", encoding="utf-8") as f:
        f.write(latex_file.build())

    # Compile the LaTeX document to PDF
    try:
        os.system("xelatex " + args["input_file"].replace(".md", ".tex"))
    except Exception as e:
        console.print(f"[red]Error compiling LaTeX document: {e}[/red]")


if __name__ == "__main__":
    main()