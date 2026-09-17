import sys
import questionary
from questionary import Style

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


def print_summary(args: dict):
    questionary.print("Here's what will run:\n", style="bold")
    for k, v in args.items():
        label = k.replace("_", " ").title()
        val = v if v not in (None, "") else "—"
        questionary.print(f"  {label:<16}", style="fg:#6C6C6C", end="")
        questionary.print(str(val), style="fg:#00d7af")
    print()


if __name__ == "__main__":
    args = run_wizard()
    print_summary(args)
    # TODO: hand off to your existing logic
    # from main import build_document
    # build_document(**args)