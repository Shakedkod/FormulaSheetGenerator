BASE_LATEX_DOC_START = r"""\documentclass[10pt]{article}
\usepackage[margin=0.6cm]{geometry}
\usepackage{polyglossia}
\usepackage{multicol}
\usepackage{amsmath, amssymb}
\usepackage{titlesec}
\usepackage{enumitem}
\usepackage{array}
\usepackage{tabularx}
\usepackage{adjustbox}

\newcolumntype{C}{>{\centering\arraybackslash}m{2cm}} % fixed-width centered

\setmainlanguage{hebrew}
\newfontfamily\hebrewfont[Script=Hebrew]{David CLM}

% Compact layout
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}

% Columns
\setlength{\columnsep}{0.4cm}
\setlength{\columnseprule}{0.2pt}

% Section styling (compact)
\titleformat{\section}{\bfseries\large}{\thesection.}{0.5em}{}
\titleformat{\subsection}{\bfseries\normalsize}{}{0em}{}
\titleformat{\subsubsection}{\bfseries\small}{}{0em}{}

\titlespacing*{\section}{0pt}{2pt}{2pt}
\titlespacing*{\subsection}{0pt}{2pt}{1pt}
\titlespacing*{\subsubsection}{0pt}{1pt}{1pt}

% Compact lists + bullet fix
\setlist[itemize]{itemsep=0pt, topsep=0pt}
\renewcommand{\labelitemi}{\raisebox{0.2ex}{\tiny$\bullet$}}
\setlength{\tabcolsep}{2pt}

\begin{document}
\small

\begin{multicols*}{3}"""

BASE_LATEX_DOC_END = r"""\end{multicols*}
\end{document}"""

LATEX_SECTION_BREAK = r"""% --- Start single-column horizontal separator ---
\noindent
\rule{\linewidth}{0.4pt}
% --- End single-column horizontal separator ---"""

def latext(text: str) -> str:
    return text.replace("&", "\\&").replace("%", "\\%").replace("#", "\\#").replace("_", "\\_").replace("{", "\\{").replace("}", "\\}")

def generate_latex_line(node: dict) -> str:
    content = ""
    
    for child in node["children"]:
        if (child["type"] == "text"):
            content += latext(child["raw"])
        elif (child["type"] == "inline_math"):
            content += f"${child['raw']}$"
        elif (child["type"] == "strong"):
            content += f"\\textbf{{{generate_latex_line(child)}}}"
        elif (child["type"] == "underline"):
            content += f"\\underline{{{generate_latex_line(child)}}}"
        elif (child["type"] == "italic"):
            content += f"\\textit{{{generate_latex_line(child)}}}"
        elif (child["type"] == "emphasis"):
            content += f"\\emph{{{generate_latex_line(child)}}}"
        elif (child["type"] == "linebreak"):
            content += " \\\\ \n"
    
    return content

def generate_latex_list(node: dict) -> str:
    if (node["type"] == "list"):
        if (node["attrs"]["ordered"]):
            content = "\\begin{enumerate}\n"
        else:
            content = "\\begin{itemize}\n"
        
        for item in node["children"]:
            for item_child in item["children"]:
                content += "\\item " + generate_latex_line(item_child) + "\n"
        
        if (node["attrs"]["ordered"]):
            content += "\\end{enumerate}"
        else:
            content += "\\end{itemize}"
        
        return content
    return ""

def generate_table(node: dict) -> str:
    content = "\\begin{center}\n\\begin{adjustbox}{max width=\columnwidth}\n\\begin{tabular}"
    # table head:
    number_of_columns = len(node["children"][0]["children"])
    content += "{|" + "C|"*number_of_columns + "}\n\\hline\n"
    
    for i in range(number_of_columns):
        last = " & "
        if (i == number_of_columns - 1):
            last = " \\\\ \n\\hline\n"
        content += generate_latex_line(node["children"][0]["children"][i]) + last
    
    # table body:
    for row in node["children"][1]["children"]:
        for i in range(number_of_columns):
            last = " & "
            if (i == number_of_columns - 1):
                last = " \\\\ \n\\hline\n"
            content += generate_latex_line(row["children"][i]) + last
    
    content += "\\end{tabular}\n\\end{adjustbox}\n\\end{center}"
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
        return (generate_latex_line(node), 0, "")
    elif (node["type"] == "block_math"):
        return (f"\\[\n{node['raw']}\n\\]", 0, "")
    elif (node["type"] == "list"):
        return (generate_latex_list(node), 0, "")
    elif (node["type"] == "table"):
        return (generate_table(node), 0, "")