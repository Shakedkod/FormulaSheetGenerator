# Formula Sheet Generator

Convert a Markdown + MathJax file into a beautifully formatted, multi-column PDF formula sheet.
Supports **Hebrew (RTL)** and **English**, with full control over layout, fonts, and colors.

---

## Requirements

- Python 3.8+
- XeLaTeX with Hebrew support:
  ```bash
  sudo apt-get install texlive-xetex texlive-lang-arabic texlive-latex-extra
  ```
- Hebrew fonts:
  ```bash
  sudo apt-get install fonts-noto
  ```

---

## Quick Start

```bash
# Hebrew, 3-column, landscape (like the sample)
python formula_sheet.py notes.md \
  --title "פיזיקה — מכניקה" \
  --subtitle "דף נוסחאות" \
  --columns 3 --landscape

# English, 2-column, dark-red theme
python formula_sheet.py notes.md -o sheet.pdf \
  --language english \
  --columns 2 \
  --main-font "Latin Modern Roman" \
  --section-color "8b0000" \
  --title-color "5c0000"
```

---

## All Options

| Flag | Default | Description |
|------|---------|-------------|
| `--columns N` | `3` | Number of columns |
| `--font-size PT` | `9` | Base font size in pt (8–12 recommended) |
| `--paper` | `a4paper` | `a4paper` / `letterpaper` / `a3paper` |
| `--landscape` | off | Landscape orientation |
| `--margin CM` | `1.2` | Page margin in cm |
| `--col-sep CM` | `0.4` | Gap between columns in cm |
| `--language` | `hebrew` | `hebrew` (RTL) or `english` (LTR) |
| `--main-font NAME` | `Noto Serif Hebrew` | XeLaTeX font name for body text |
| `--math-font NAME` | *(auto)* | Math font (leave empty for Latin Modern Math) |
| `--mono-font NAME` | `DejaVu Sans Mono` | Monospace font for `code` |
| `--title TEXT` | — | Title text at top of sheet |
| `--subtitle TEXT` | — | Subtitle below title |
| `--no-title` | — | Hide the title block |
| `--title-color HEX` | `1a1a6e` | Title color (HTML hex, no #) |
| `--section-color HEX` | `2c2c8a` | Section heading color |
| `--box-color HEX` | `e8e8f8` | Display math box background |
| `--bg-color HEX` | *(white)* | Page background color |
| `--rule-color HEX` | `9999bb` | Horizontal rule / border color |
| `--no-section-box` | — | Plain headings instead of colored boxes |
| `--show-frame` | — | Show column separator line |

---

## Markdown Syntax Reference

```markdown
# Section heading          → large colored box/heading
## Subsection              → medium heading with rule
### Sub-subsection         → small bold heading

**bold**  *italic*  `code`

- bullet item              → compact list
1. numbered item           → numbered list

> This is a note box       → yellow highlighted note

$$                         → display math (boxed)
E = mc^2
$$

$E = mc^2$                 → inline math

---                        → horizontal rule
```

---

## Font Recommendations

### Hebrew sheets
| Font | Notes |
|------|-------|
| `Noto Serif Hebrew` | Excellent, includes all weights |
| `Noto Sans Hebrew` | Clean sans-serif variant |
| `David CLM` | Classic Israeli style (needs culmus package) |

### English sheets
| Font | Notes |
|------|-------|
| `Latin Modern Roman` | Default LaTeX serif — great for math |
| `TeX Gyre Termes` | Times-style, very readable |
| `DejaVu Serif` | Good Unicode coverage |
| `Liberation Serif` | Arial/Times-compatible |

---

## Output Files

For each run, two files are produced:
- `output.pdf` — the formatted formula sheet
- `output.tex` — the generated LaTeX source (edit manually if needed, then run `xelatex` directly)

---

## Examples

```bash
# Compact single-page sheet (tiny font, small margins)
python formula_sheet.py notes.md \
  --columns 4 --font-size 8 --margin 0.8 --landscape \
  --title "Quick Reference"

# Dark theme
python formula_sheet.py notes.md \
  --bg-color "1a1a2e" \
  --section-color "e0e0ff" \
  --title-color "ffffff" \
  --box-color "2a2a4e" \
  --rule-color "555577"

# No decorations, minimal style
python formula_sheet.py notes.md \
  --no-section-box \
  --no-title \
  --columns 2
```