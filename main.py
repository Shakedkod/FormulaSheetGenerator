#!/usr/bin/env python3
"""
Formula Sheet Generator
Converts Markdown + MathJax files into a beautifully formatted PDF formula sheet.
Supports English and Hebrew (RTL), configurable columns, fonts, colors, and page limits.

Usage:
    python formula_sheet.py input.md -o output.pdf [options]
"""

import argparse
import re
import subprocess
import sys
import os
import shutil
import tempfile
from dataclasses import dataclass
from typing import Optional


# ─────────────────────────────────────────────────────────────────────────────
#  Configuration
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class SheetConfig:
    # Layout
    columns: int = 3
    paper: str = "a4paper"          # a4paper | letterpaper | a3paper
    font_size: int = 9               # pts: 8-12 recommended
    margin_cm: float = 1.2
    col_sep_cm: float = 0.4
    landscape: bool = False

    # Language
    language: str = "hebrew"         # "hebrew" | "english"

    # Fonts (XeLaTeX font names)
    main_font: str = "Noto Serif Hebrew"
    math_font: str = ""              # "" = use Latin Modern Math (default)
    mono_font: str = "DejaVu Sans Mono"

    # Colors (HTML hex, no #)
    title_color: str = "1a1a6e"
    section_color: str = "2c2c8a"
    subsection_color: str = "3a3a3a"
    rule_color: str = "9999bb"
    box_color: str = "e8e8f8"        # display math box background
    bg_color: str = ""               # page background; "" = white

    # Title block
    title: str = ""
    subtitle: str = ""
    show_title: bool = True

    # Styling
    section_box: bool = True         # colored box behind section headings
    show_frame: bool = False         # column separator rule
    compact_lists: bool = True


# ─────────────────────────────────────────────────────────────────────────────
#  Markdown → LaTeX conversion
# ─────────────────────────────────────────────────────────────────────────────

class MarkdownConverter:
    """
    Converts Markdown+MathJax to LaTeX.
    Supported syntax:
        # / ## / ###  headings
        **bold**  *italic*  `code`
        - / * / 1.  lists
        > blockquote → note box
        $$...$$  display math
        $...$    inline math
        ---      horizontal rule
    """

    def __init__(self, config: SheetConfig):
        self.cfg = config
        self.in_list = False
        self.list_type = None

    def convert(self, md_text: str) -> str:
        lines = md_text.splitlines()
        out = []
        i = 0
        while i < len(lines):
            line = lines[i]
            stripped = line.strip()

            # ── Display math block  $$...$$ ────────────────────────────────
            if stripped.startswith("$$"):
                self._close_list(out)
                inner = stripped[2:]
                # single-line $$...$$ or multi-line
                if inner.endswith("$$") and len(inner) > 2:
                    math_body = inner[:-2].strip()
                    i += 1
                else:
                    math_lines = [inner] if inner else []
                    i += 1
                    while i < len(lines):
                        nl = lines[i].strip()
                        if nl.endswith("$$"):
                            math_lines.append(nl[:-2])
                            i += 1
                            break
                        math_lines.append(lines[i])
                        i += 1
                    math_body = "\n".join(math_lines).strip()
                out.append(r"\begin{formulamath}" + "\n" +
                           math_body + "\n" +
                           r"\end{formulamath}")
                out.append("")
                continue

            # ── Horizontal rule ────────────────────────────────────────────
            if re.match(r"^[-*_]{3,}\s*$", stripped):
                self._close_list(out)
                out.append(r"\formulahrule")
                i += 1
                continue

            # ── Headings ───────────────────────────────────────────────────
            m = re.match(r"^(#{1,4})\s+(.*)", line)
            if m:
                self._close_list(out)
                level = len(m.group(1))
                text = self._inline(m.group(2))
                out.append(self._heading(level, text))
                i += 1
                continue

            # ── Blockquote ─────────────────────────────────────────────────
            if stripped.startswith(">"):
                self._close_list(out)
                content_lines = [stripped[1:].strip()]
                i += 1
                while i < len(lines) and lines[i].strip().startswith(">"):
                    content_lines.append(lines[i].strip()[1:].strip())
                    i += 1
                content = " ".join(content_lines)
                out.append(r"\begin{formulanote}")
                out.append(self._inline(content))
                out.append(r"\end{formulanote}")
                out.append("")
                continue

            # ── Unordered list ─────────────────────────────────────────────
            m_ul = re.match(r"^(\s*)[-*+]\s+(.*)", line)
            if m_ul:
                if not self.in_list or self.list_type != "itemize":
                    self._close_list(out)
                    out.append(r"\begin{itemize}")
                    self.in_list = True
                    self.list_type = "itemize"
                out.append(r"\item " + self._inline(m_ul.group(2)))
                i += 1
                continue

            # ── Ordered list ───────────────────────────────────────────────
            m_ol = re.match(r"^\s*\d+[.)]\s+(.*)", line)
            if m_ol:
                if not self.in_list or self.list_type != "enumerate":
                    self._close_list(out)
                    out.append(r"\begin{enumerate}")
                    self.in_list = True
                    self.list_type = "enumerate"
                out.append(r"\item " + self._inline(m_ol.group(1)))
                i += 1
                continue

            # ── Empty line ─────────────────────────────────────────────────
            if stripped == "":
                self._close_list(out)
                out.append("")
                i += 1
                continue

            # ── Regular text ───────────────────────────────────────────────
            self._close_list(out)
            out.append(self._inline(line))
            i += 1

        self._close_list(out)
        return "\n".join(out)

    def _close_list(self, out):
        if self.in_list:
            out.append(r"\end{" + self.list_type + "}")
            out.append("")
            self.in_list = False
            self.list_type = None

    def _heading(self, level: int, text: str) -> str:
        cmds = {1: "formulasection", 2: "formulasubsection",
                3: "formulasubsubsection", 4: "textbf"}
        cmd = cmds.get(level, "textbf")
        return rf"\{cmd}{{{text}}}"

    def _inline(self, text: str) -> str:
        """Process inline Markdown → LaTeX."""
        # First, split on inline math segments to avoid escaping inside math
        # We tokenize: math segments stay untouched, text segments get processed
        parts = re.split(r"(\$[^\$]+?\$)", text)
        result = []
        for i, part in enumerate(parts):
            if part.startswith("$") and part.endswith("$"):
                result.append(part)  # math: keep as-is
            else:
                p = part
                # Escape special LaTeX chars (outside math)
                p = p.replace("&", r"\&")
                p = p.replace("%", r"\%")
                p = p.replace("#", r"\#")
                p = p.replace("_", r"\_")
                p = p.replace("^", r"\^{}")
                p = p.replace("~", r"\textasciitilde{}")
                # Bold+italic ***...***
                p = re.sub(r"\*\*\*(.*?)\*\*\*", r"\\textbf{\\textit{\1}}", p)
                # Bold **...**
                p = re.sub(r"\*\*(.*?)\*\*", r"\\textbf{\1}", p)
                # Italic *...*
                p = re.sub(r"\*([^*]+)\*", r"\\textit{\1}", p)
                # Inline code `...`
                p = re.sub(r"`([^`]+)`", r"\\texttt{\1}", p)
                result.append(p)
        return "".join(result)


# ─────────────────────────────────────────────────────────────────────────────
#  LaTeX document builder
# ─────────────────────────────────────────────────────────────────────────────

class LaTeXBuilder:
    def __init__(self, config: SheetConfig):
        self.cfg = config

    def _is_rtl(self) -> bool:
        return self.cfg.language.lower() in ("hebrew", "he")

    # ── Preamble ──────────────────────────────────────────────────────────────

    def build_preamble(self) -> str:
        c = self.cfg
        lo = ",landscape" if c.landscape else ""

        lines = []
        lines.append(rf"\documentclass[{c.font_size}pt,{c.paper}{lo}]{{article}}")

        # Packages
        lines.append(r"""
\usepackage{fontspec}
\usepackage{amsmath,amssymb,mathtools}
\usepackage{unicode-math}
\usepackage{xcolor}
\usepackage{geometry}
\usepackage{multicol}
\usepackage[most,breakable]{tcolorbox}
\usepackage{enumitem}
\usepackage{parskip}
""")

        # Language
        if self._is_rtl():
            lines.append(r"""
\usepackage{polyglossia}
\setmainlanguage{hebrew}
\setotherlanguage{english}
""")
        else:
            lines.append(r"""
\usepackage{polyglossia}
\setmainlanguage{english}
""")

        # Fonts
        lines.append(rf"\setmainfont{{{c.main_font}}}")
        lines.append(rf"\setmonofont{{{c.mono_font}}}[Scale=MatchLowercase]")
        if c.math_font:
            lines.append(rf"\setmathfont{{{c.math_font}}}")

        # Geometry
        lines.append(rf"""
\geometry{{
    {c.paper},
    {"landscape," if c.landscape else ""}%
    margin={c.margin_cm}cm,
    columnsep={c.col_sep_cm}cm
}}
""")

        # Color definitions
        lines.append(rf"""
\definecolor{{titlecolor}}{{HTML}}{{{c.title_color}}}
\definecolor{{sectioncolor}}{{HTML}}{{{c.section_color}}}
\definecolor{{subsectioncolor}}{{HTML}}{{{c.subsection_color}}}
\definecolor{{rulecolor}}{{HTML}}{{{c.rule_color}}}
\definecolor{{boxcolor}}{{HTML}}{{{c.box_color}}}
""")
        if c.bg_color:
            lines.append(rf"""
\definecolor{{bgcolor}}{{HTML}}{{{c.bg_color}}}
\pagecolor{{bgcolor}}
""")

        # List spacing
        if c.compact_lists:
            lines.append(r"""
\setlist{nosep, leftmargin=1.2em, topsep=1pt, itemsep=0pt, parsep=0pt}
""")

        # ── Custom commands ──────────────────────────────────────────────────

        # Section heading: boxed or plain
        if c.section_box:
            lines.append(r"""
\newcommand{\formulasection}[1]{%
  \vspace{5pt}%
  \begin{tcolorbox}[
      colback=sectioncolor!12,
      colframe=sectioncolor,
      boxrule=0.7pt, arc=2pt,
      left=3pt, right=3pt, top=1.5pt, bottom=1.5pt,
      before skip=5pt, after skip=3pt
  ]
  {\bfseries\color{sectioncolor}\large #1}%
  \end{tcolorbox}%
}
""")
        else:
            lines.append(r"""
\newcommand{\formulasection}[1]{%
  \vspace{5pt}%
  {\bfseries\color{sectioncolor}\large #1}\par\vspace{1pt}%
  {\color{sectioncolor}\hrule height 0.8pt}\vspace{3pt}%
}
""")

        lines.append(r"""
\newcommand{\formulasubsection}[1]{%
  \vspace{3pt}%
  {\bfseries\color{subsectioncolor}\normalsize #1}\par\vspace{0.5pt}%
  {\color{rulecolor}\hrule height 0.4pt}\vspace{2pt}%
}

\newcommand{\formulasubsubsection}[1]{%
  \vspace{2pt}{\bfseries\small #1}\par%
}

\newcommand{\formulahrule}{%
  \vspace{2pt}{\color{rulecolor}\hrule height 0.4pt}\vspace{2pt}%
}
""")

        # Display math environment
        lines.append(r"""
\tcbset{mathbox/.style={
    colback=boxcolor!70,
    colframe=rulecolor,
    boxrule=0.5pt, arc=2pt,
    left=4pt, right=4pt, top=2pt, bottom=2pt,
    before skip=3pt, after skip=3pt,
    breakable
}}
\newenvironment{formulamath}{%
  \begin{tcolorbox}[mathbox]%
  \begin{equation*}%
}{%
  \end{equation*}%
  \end{tcolorbox}%
}
""")

        # Note / blockquote environment
        lines.append(r"""
\newenvironment{formulanote}{%
  \begin{tcolorbox}[
      colback=yellow!8,
      colframe=yellow!50!black,
      boxrule=0.5pt, arc=2pt,
      left=4pt, right=4pt, top=2pt, bottom=2pt,
      before skip=3pt, after skip=3pt,
      breakable
  ]\small%
}{%
  \end{tcolorbox}%
}
""")

        # Paragraph settings
        lines.append(r"""
\setlength{\parskip}{2pt}
\setlength{\parindent}{0pt}
""")

        return "\n".join(lines)

    # ── Title block ───────────────────────────────────────────────────────────

    def build_title(self) -> str:
        c = self.cfg
        if not c.show_title or (not c.title and not c.subtitle):
            return ""
        parts = [r"\begin{center}"]
        if c.title:
            parts.append(
                rf"{{\LARGE\bfseries\color{{titlecolor}} {c.title}}}\\"
            )
        if c.subtitle:
            parts.append(
                rf"{{\small\color{{subsectioncolor}} {c.subtitle}}}\\"
            )
        parts.append(r"\end{center}")
        parts.append(r"\vspace{1pt}{\color{rulecolor}\hrule height 1pt}\vspace{4pt}")
        return "\n".join(parts)

    # ── Full document ─────────────────────────────────────────────────────────

    def build_document(self, body_latex: str) -> str:
        c = self.cfg
        doc = self.build_preamble() + "\n\\begin{document}\n"

        if self._is_rtl():
            doc += r"\begin{hebrew}" + "\n"

        doc += self.build_title() + "\n"
        doc += rf"\setlength{{\columnsep}}{{{c.col_sep_cm}cm}}" + "\n"

        if c.show_frame:
            doc += r"\setlength{\columnseprule}{0.4pt}" + "\n"

        doc += rf"\begin{{multicols}}{{{c.columns}}}" + "\n"
        doc += body_latex + "\n"
        doc += r"\end{multicols}" + "\n"

        if self._is_rtl():
            doc += r"\end{hebrew}" + "\n"

        doc += r"\end{document}" + "\n"
        return doc


# ─────────────────────────────────────────────────────────────────────────────
#  PDF Compiler
# ─────────────────────────────────────────────────────────────────────────────

class PDFCompiler:
    def __init__(self, workdir: str):
        self.workdir = workdir

    def compile(self, tex_source: str, output_pdf: str, runs: int = 2) -> bool:
        tex_path = os.path.join(self.workdir, "sheet.tex")
        with open(tex_path, "w", encoding="utf-8") as f:
            f.write(tex_source)

        for run in range(runs):
            result = subprocess.run(
                ["xelatex", "-interaction=nonstopmode", "-halt-on-error", "sheet.tex"],
                cwd=self.workdir,
                capture_output=True,
                text=True
            )
            if result.returncode != 0:
                print("\n── XeLaTeX Error ──")
                # Show errors and relevant lines
                for line in result.stdout.split("\n"):
                    if any(k in line for k in ("Error", "error", "!", "undefined",
                                                "Undefined", "missing", "Missing")):
                        print(line)
                print("Full log saved to:", os.path.join(self.workdir, "sheet.log"))
                log_path = os.path.join(self.workdir, "sheet.log")
                if os.path.exists(log_path):
                    shutil.copy2(log_path, output_pdf.replace(".pdf", "_error.log"))
                return False

        pdf_in = os.path.join(self.workdir, "sheet.pdf")
        if os.path.exists(pdf_in):
            shutil.copy2(pdf_in, output_pdf)
            return True
        return False


# ─────────────────────────────────────────────────────────────────────────────
#  Main pipeline
# ─────────────────────────────────────────────────────────────────────────────

def generate(md_file: str, output_pdf: str, config: SheetConfig) -> bool:
    with open(md_file, "r", encoding="utf-8") as f:
        md_text = f.read()

    print(f"📄 Parsing: {md_file}")
    converter = MarkdownConverter(config)
    body_latex = converter.convert(md_text)

    builder = LaTeXBuilder(config)
    full_tex = builder.build_document(body_latex)

    # Save .tex alongside the output for inspection/editing
    tex_out = output_pdf.replace(".pdf", ".tex")
    with open(tex_out, "w", encoding="utf-8") as f:
        f.write(full_tex)
    print(f"✔ LaTeX source → {tex_out}")

    print("⚙  Compiling with XeLaTeX…")
    with tempfile.TemporaryDirectory() as tmpdir:
        compiler = PDFCompiler(tmpdir)
        ok = compiler.compile(full_tex, output_pdf)

    if ok:
        size_kb = os.path.getsize(output_pdf) // 1024
        print(f"✔ PDF ready → {output_pdf}  ({size_kb} KB)")
    else:
        print("✘ Compilation failed. The .tex file has been saved for manual debugging.")
    return ok


# ─────────────────────────────────────────────────────────────────────────────
#  CLI
# ─────────────────────────────────────────────────────────────────────────────

def build_parser():
    p = argparse.ArgumentParser(
        description="Convert Markdown+MathJax → formula-sheet PDF",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    p.add_argument("input", help="Input .md file")
    p.add_argument("-o", "--output", default="formula_sheet.pdf",
                   help="Output PDF path")

    g = p.add_argument_group("Layout")
    g.add_argument("--columns", type=int, default=3, metavar="N",
                   help="Number of columns")
    g.add_argument("--font-size", type=int, default=9, metavar="PT",
                   help="Base font size (pt)")
    g.add_argument("--paper", default="a4paper",
                   choices=["a4paper", "letterpaper", "a3paper"])
    g.add_argument("--landscape", action="store_true")
    g.add_argument("--margin", type=float, default=1.2,
                   metavar="CM", help="Page margin (cm)")
    g.add_argument("--col-sep", type=float, default=0.4,
                   metavar="CM", help="Column separator (cm)")

    g2 = p.add_argument_group("Language & Fonts")
    g2.add_argument("--language", default="hebrew",
                    choices=["hebrew", "english"])
    g2.add_argument("--main-font", default="Noto Serif Hebrew")
    g2.add_argument("--math-font", default="",
                    help="Math font (empty = Latin Modern Math)")
    g2.add_argument("--mono-font", default="DejaVu Sans Mono")

    g3 = p.add_argument_group("Colors (HTML hex, no #)")
    g3.add_argument("--title-color", default="1a1a6e")
    g3.add_argument("--section-color", default="2c2c8a")
    g3.add_argument("--box-color", default="e8e8f8",
                    help="Display math box background")
    g3.add_argument("--bg-color", default="",
                    help="Page background (empty = white)")
    g3.add_argument("--rule-color", default="9999bb")

    g4 = p.add_argument_group("Title")
    g4.add_argument("--title", default="", help="Title text")
    g4.add_argument("--subtitle", default="", help="Subtitle text")
    g4.add_argument("--no-title", action="store_true")

    g5 = p.add_argument_group("Style")
    g5.add_argument("--no-section-box", action="store_true",
                    help="Plain section headings instead of boxes")
    g5.add_argument("--show-frame", action="store_true",
                    help="Show column separator rule")

    return p


def main():
    args = build_parser().parse_args()
    cfg = SheetConfig(
        columns=args.columns,
        font_size=args.font_size,
        paper=args.paper,
        landscape=args.landscape,
        margin_cm=args.margin,
        col_sep_cm=args.col_sep,
        language=args.language,
        main_font=args.main_font,
        math_font=args.math_font,
        mono_font=args.mono_font,
        title_color=args.title_color,
        section_color=args.section_color,
        box_color=args.box_color,
        bg_color=args.bg_color,
        rule_color=args.rule_color,
        title=args.title,
        subtitle=args.subtitle,
        show_title=not args.no_title,
        section_box=not args.no_section_box,
        show_frame=args.show_frame,
    )
    ok = generate(args.input, args.output, cfg)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()