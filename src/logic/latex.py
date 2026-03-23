BASE_LATEX_DOC_START = r"""\documentclass{article}
\usepackage[margin=0.8cm, top=1cm, bottom=1cm]{geometry}
\usepackage{polyglossia}
\usepackage{multicol}

% Define Hebrew as the main language
\setmainlanguage{hebrew}
\newfontfamily\hebrewfont[Script=Hebrew]{David CLM}

% Optional: Adjust the space between columns and add a divider line
\setlength{\columnsep}{0.5cm}
\setlength{\columnseprule}{0.4pt}

% Document
\begin{document}
\begin{multicols*}{3}"""

BASE_LATEX_DOC_END = r"""\end{multicols*}
\end{document}"""

LATEX_SECTION_BREAK = r"""% --- Start single-column horizontal separator ---
\noindent
\rule{\linewidth}{0.4pt}
% --- End single-column horizontal separator ---"""

def latext(text: str) -> str:
    return text.replace("&", "\\&").replace("%", "\\%").replace("#", "\\#").replace("_", "\\_").replace("{", "\\{").replace("}", "\\}")

def fix_mathjax_latex_arrays(latex: str) -> str:
    pass

def generate_latex_line(node: dict) -> str:
    content = ""
    
    for child in node["children"]:
        if (child["type"] == "text"):
            content += latext(child["raw"])
        elif (child["type"] == "inline_math"):
            content += f"${child['raw']}$"
    
    return content

def generate_latex_from_node(node: dict, section_num: int) -> tuple[str, int, str]:
    if (node["type"] == "heading"):
        if (node["attrs"]["level"] == 1):
            if (section_num > 1):
                return (LATEX_SECTION_BREAK + "\n" + f"\\section{{{generate_latex_line(node)}}}", 1, "")
            return (f"\\section{{{generate_latex_line(node)}}}", 1, "")
        elif (node["attrs"]["level"] == 2):
            return (f"\\subsection{{{generate_latex_line(node)}}}", 0, "")
        elif (node["attrs"]["level"] == 3):
            return (f"\\subsubsection{{{generate_latex_line(node)}}}", 0, "")
    elif (node["type"] == "blank_line"):
        return ("", 0, "")
    elif (node["type"] == "paragraph"):
        return (generate_latex_line(node), 0, " \\\\")
    elif (node["type"] == "block_math"):
        return (f"\\[\n{node['raw']}\n\\]", 0, "")