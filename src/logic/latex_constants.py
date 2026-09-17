BASE_LATEX_DOC_START = r"""% ============================================================
% === Created by MDtoLatex - A Markdown to LaTeX Converter ===
% ====== ShakedKod, 2026 - https://github.com/ShakedKod ======
% ============================================================
\documentclass[12pt]{article}"""

BASE_LATEX_TEXT = r"""% ---------- Fonts & language ----------
\usepackage{hyperref}
\usepackage{fontspec}
"""

LATEX_HEBREW_TEXT = r"""\usepackage{polyglossia}
\setdefaultlanguage{hebrew}
\setotherlanguage{english}
\newfontfamily\titlefont{Nachlieli CLM}
\newfontfamily\hebrewfont{David CLM}
\newfontfamily{\hebrewfonttt}[Script=Hebrew]{David CLM}
\newfontfamily\englishfont{Latin Modern Roman}

\renewcommand\labelitemi{$\bullet$}
\renewcommand\labelitemii{$\circ$}
\renewcommand\labelitemiii{$\ast$}
\renewcommand\labelitemiv{$\cdot$}
"""

BASE_LATEX_MATH = r"""% ---------- Math ----------
\usepackage{amsmath, amssymb, amsthm, mathtools, cancel}
\usepackage{bm}          % \bm for bold math (vectors etc.)
\usepackage{physics}     % bra-ket, derivatives — optional, remove if unused
\usepackage{adjustbox}   % fit math in tables"""

BASE_LATEX_PAGE_LAYOUT = r"""% ---------- Page Layout ----------
\usepackage{fancyhdr, fancy}
\usepackage{lastpage}

\pagestyle{fancy}
\fancyhf{} % clear all header and footer fields
"""

LATEX_IMAGES_AND_DIAGRAMS = r"""% ---------- Images & Diagrams ----------
\usepackage{relsize, graphicx, svg, geometry}
"""

LATEX_TIKZ = r"""\usepackage{tikz, circuitikz}
\usetikzlibrary{quotes, angles, shapes.gates.logic.US}
\usetikzlibrary{arrows.meta, automata, positioning, calc, shapes.geometric, backgrounds, fit}
\newcommand{\tikzmark}[1]{\tikz[overlay,remember picture] \coordinate (#1);}
\geometry{margin=2.5cm}
"""

BASIC_LATEX_MISC = r"""% ---------- Misc quality-of-life ----------
\usepackage[toc]{appendix}
\PassOptionsToPackage{prologue}{xcolor}
\usepackage{xcolor, diagbox}
\usepackage{titling, longtable, booktabs, array}
\usepackage{parskip}

\definecolor{linkblue}{HTML}{0997E6}
\renewcommand{\appendixpagename}{נספחים}
\renewcommand{\appendixtocname}{נספחים}

% section numbering depth & making sure the paragraph and subparagraph levels are numbered and appear correctly
\setcounter{secnumdepth}{5} 
\setcounter{tocdepth}{5}

\makeatletter
\renewcommand\paragraph{\@startsection{paragraph}{4}{\z@}%
  {-3.25ex\@plus -1ex \@minus -.2ex}%
  {1.5ex \@plus .2ex}%
  {\normalfont\normalsize\bfseries}}
\renewcommand\subparagraph{\@startsection{subparagraph}{5}{\z@}%
  {-3.25ex\@plus -1ex \@minus -.2ex}%
  {1.5ex \@plus .2ex}%
  {\normalfont\normalsize\bfseries}}
\makeatletter
"""

LATEX_THEME_REGULAR = r"""% ---------- Regular Theme ----------
\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]      % thm
\newtheorem{lemma}[theorem]{Lemma}          % lem
\newtheorem{proposition}[theorem]{Proposition}   % prp
\newtheorem{corollary}[theorem]{Corollary}    % cor
\newtheorem{claim}[theorem]{Claim}     % clm
\newtheorem{conjecture}[theorem]{Conjecture}   % cnj

\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}   % def
\newtheorem{axiom}[theorem]{Axiom}      % axm
\newtheorem{assumption}[theorem]{Assumption}    % asm
\newtheorem{example}[theorem]{Example}      % exm
\newtheorem{exercise}[theorem]{Exercise}     % exr
\newtheorem{hypothesis}[theorem]{Hypothesis} % hyp

\theoremstyle{remark}
\newtheorem*{remark}{Remark}                % rmk

\makeatletter
\renewenvironment{proof}[1][\proofname]{\par
  \pushQED{\qed}%
  \normalfont \topsep6\p@\@plus6\p@\relax
  \trivlist
  \item[\hskip\labelsep\itshape #1\@addpunct{.}]\par\ignorespaces
}{%
  \popQED\endtrivlist\@endpefalse
}
\renewcommand{\qed}{\par\nobreak\hfill\qedsymbol\par}
\makeatother
\renewcommand{\proofname}{Proof}          % Proof
"""

LATEX_THEME_REGULAR_HEBREW = r"""% ---------- Regular Theme ----------
\theoremstyle{plain}
\newtheorem{theorem}{משפט}[section]      % thm
\newtheorem{lemma}[theorem]{למה}          % lem
\newtheorem{proposition}[theorem]{טענה}   % prp
\newtheorem{corollary}[theorem]{מסקנה}    % cor
\newtheorem{claim}[theorem]{טענה עזר}     % clm
\newtheorem{conjecture}[theorem]{השערה}   % cnj

\theoremstyle{definition}
\newtheorem{definition}[theorem]{הגדרה}   % def
\newtheorem{axiom}[theorem]{אקסיומה}      % axm
\newtheorem{assumption}[theorem]{הנחה}    % asm
\newtheorem{example}[theorem]{דוגמה}      % exm
\newtheorem{exercise}[theorem]{תרגיל}     % exr
\newtheorem{hypothesis}[theorem]{השערת עבודה} % hyp

\theoremstyle{remark}
\newtheorem*{remark}{הערה}                % rmk

\makeatletter
\renewenvironment{proof}[1][\proofname]{\par
  \pushQED{\qed}%
  \normalfont \topsep6\p@\@plus6\p@\relax
  \trivlist
  \item[\hskip\labelsep\itshape #1\@addpunct{.}]\par\ignorespaces
}{%
  \popQED\endtrivlist\@endpefalse
}
\renewcommand{\qed}{\par\nobreak\hfill\qedsymbol\par}
\makeatother
\renewcommand{\proofname}{הוכחה}          % הוכחה
"""

LATEX_CODEBLOCK_SETUP = r"""\usepackage{listings}
% ---------- Assembler Codeblock Setup ----------
% Define colors
\definecolor{commentgreen}{rgb}{0,0.6,0}
\definecolor{keywordblue}{rgb}{0,0,0.8}
\definecolor{registerpurple}{rgb}{0.5,0,0.5}
\definecolor{stringorange}{rgb}{0.8,0.4,0}
\definecolor{gold}{HTML}{FFD700}
\definecolor{myblue}{RGB}{37,97,175}

% Define the RISC-V Language Dialect
\lstdefinelanguage{assembly}{
    alsoletter={.}, % Allow dots in keywords like .text or .global
    alsodigit={0x}, % Properly identify hex values
    morekeywords=[1]{ % Core RISC-V Instructions
        add, addi, sub, lui, auipc, xor, xori, or, ori, and, andi,
        sll, slli, srl, srli, sra, srai, slt, slti, sltu, sltiu,
        beq, bne, blt, bge, bltu, bgeu, jal, jalr, lw, lh, lb,
        lbu, lhu, sw, sh, sb, ECALL, ecall, EBREAK, ebreak,
        % Common Pseudoinstructions
        li, la, mv, not, neg, seqz, snez, sltz, sgtz,
        j, jr, jal, ret, call, tail, nop
    },
    morekeywords=[2]{ % RISC-V Registers (ABI and Symbolic names)
        x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15,
        x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31,
        zero, ra, sp, gp, tp, t0, t1, t2, s0, fp, s1, a0, a1, a2, a3, a4, a5, a6, a7,
        s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, t3, t4, t5, t6
    },
    morekeywords=[3]{ % Assembler Directives
        .text, .data, .rodata, .bss, .globl, .global, .align, .word, .half, .byte, .asciiz, .string, .section
    },
    showstringspaces=false,
    morecomment=[l]{\#},      % Standard RISC-V comments start with #
    morecomment=[l]{;},       % Fallback comment style
    morestring=[b]",          % Double quotes strings
    morestring=[b]'           % Single quotes strings
}[keywords,comments,strings]

\lstdefinelanguage{Assembler}{
    alsoletter={.}, % Allow dots in keywords like .text or .global
    alsodigit={0x}, % Properly identify hex values
    morekeywords=[1]{ % Core RISC-V Instructions
        add, addi, sub, lui, auipc, xor, xori, or, ori, and, andi,
        sll, slli, srl, srli, sra, srai, slt, slti, sltu, sltiu,
        beq, bne, blt, bge, bltu, bgeu, jal, jalr, lw, lh, lb,
        lbu, lhu, sw, sh, sb, ECALL, ecall, EBREAK, ebreak,
        % Common Pseudoinstructions
        li, la, mv, not, neg, seqz, snez, sltz, sgtz,
        j, jr, jal, ret, call, tail, nop
    },
    morekeywords=[2]{ % RISC-V Registers (ABI and Symbolic names)
        x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15,
        x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31,
        zero, ra, sp, gp, tp, t0, t1, t2, s0, fp, s1, a0, a1, a2, a3, a4, a5, a6, a7,
        s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, t3, t4, t5, t6
    },
    morekeywords=[3]{ % Assembler Directives
        .text, .data, .rodata, .bss, .globl, .global, .align, .word, .half, .byte, .asciiz, .string, .section
    },
    showstringspaces=false,
    morecomment=[l]{\#},      % Standard RISC-V comments start with #
    morecomment=[l]{;},       % Fallback comment style
    morestring=[b]",          % Double quotes strings
    morestring=[b]'           % Single quotes strings
}[keywords,comments,strings]

\lstdefinelanguage{asm}{
    alsoletter={.}, % Allow dots in keywords like .text or .global
    alsodigit={0x}, % Properly identify hex values
    morekeywords=[1]{ % Core RISC-V Instructions
        add, addi, sub, lui, auipc, xor, xori, or, ori, and, andi,
        sll, slli, srl, srli, sra, srai, slt, slti, sltu, sltiu,
        beq, bne, blt, bge, bltu, bgeu, jal, jalr, lw, lh, lb,
        lbu, lhu, sw, sh, sb, ECALL, ecall, EBREAK, ebreak,
        % Common Pseudoinstructions
        li, la, mv, not, neg, seqz, snez, sltz, sgtz,
        j, jr, jal, ret, call, tail, nop
    },
    morekeywords=[2]{ % RISC-V Registers (ABI and Symbolic names)
        x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15,
        x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31,
        zero, ra, sp, gp, tp, t0, t1, t2, s0, fp, s1, a0, a1, a2, a3, a4, a5, a6, a7,
        s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, t3, t4, t5, t6
    },
    morekeywords=[3]{ % Assembler Directives
        .text, .data, .rodata, .bss, .globl, .global, .align, .word, .half, .byte, .asciiz, .string, .section
    },
    showstringspaces=false,
    morecomment=[l]{\#},      % Standard RISC-V comments start with #
    morecomment=[l]{;},       % Fallback comment style
    morestring=[b]",          % Double quotes strings
    morestring=[b]'           % Single quotes strings
}[keywords,comments,strings]

\lstdefinelanguage{riscv}{
    alsoletter={.}, % Allow dots in keywords like .text or .global
    alsodigit={0x}, % Properly identify hex values
    morekeywords=[1]{ % Core RISC-V Instructions
        add, addi, sub, lui, auipc, xor, xori, or, ori, and, andi,
        sll, slli, srl, srli, sra, srai, slt, slti, sltu, sltiu,
        beq, bne, blt, bge, bltu, bgeu, jal, jalr, lw, lh, lb,
        lbu, lhu, sw, sh, sb, ECALL, ecall, EBREAK, ebreak,
        % Common Pseudoinstructions
        li, la, mv, not, neg, seqz, snez, sltz, sgtz,
        j, jr, jal, ret, call, tail, nop
    },
    morekeywords=[2]{ % RISC-V Registers (ABI and Symbolic names)
        x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15,
        x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31,
        zero, ra, sp, gp, tp, t0, t1, t2, s0, fp, s1, a0, a1, a2, a3, a4, a5, a6, a7,
        s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, t3, t4, t5, t6
    },
    morekeywords=[3]{ % Assembler Directives
        .text, .data, .rodata, .bss, .globl, .global, .align, .word, .half, .byte, .asciiz, .string, .section
    },
    showstringspaces=false,
    morecomment=[l]{\#},      % Standard RISC-V comments start with #
    morecomment=[l]{;},       % Fallback comment style
    morestring=[b]",          % Double quotes strings
    morestring=[b]'           % Single quotes strings
}[keywords,comments,strings]

% Apply Styles globally to the document
\lstset{
    basicstyle={\small\ttfamily},
    keywordstyle=[1]\color{keywordblue}\bfseries,
    keywordstyle=[2]\color{registerpurple},
    keywordstyle=[3]\color{gray}\bfseries,
    commentstyle=\color{commentgreen}\itshape,
    stringstyle=\color{stringorange},
    numbers=left,
    numberstyle=\tiny\color{gray},
    frame=single,
    tabsize=4,
    breaklines=true
}
"""

START_OF_DOCUMENT_CONTENT = r"""
% ============================================================
% THE START OF THE DOCUMENT CONTENT
% ============================================================
\begin{document}
\maketitle
"""

LATEX_TABLE_OF_CONTENTS = r"""\tableofcontents
\newpage
"""

EXTRA_LATEX_PACKAGES_HEADER = r"""% ---------- Extra LaTeX Packages ----------
"""

CREDIT_BOX = r"""\vspace{2cm}
\begin{center}
\fbox{
    \begin{minipage}{0.9\textwidth}
        \vspace{0.2cm} % מרווח קטן בחלק העליון
        \begin{center} % מרכוז הטקסט בתוך הקופסה
            רשימות אלו נלקחו מהאתם {\color{linkblue}\underline{\href{https://uni-folder.vercel.app/}{uni-folder}}} מוזמנים לבקר שם ולראות סיכומים נוספים.

            \vspace{0.3cm}

            כל הסיכום הזה אינו מובטח להיות מלא או נכון ב-\(100\%\). יכולות להיות פה טעויות כתיב ואף טעויות בחומר. אם אתם מוצאים כאלו מוזמנים לשלוח לי במייל(shaqued.k@campus.technion.ac.il) או בכל דרך אחרת.
        \end{center}
        \vspace{0.1cm} % מרווח קטן בחלק התחתון
    \end{minipage}
}
\end{center}
\vspace{2cm}
"""

BASE_LATEX_DOC_END = r"""\end{document}"""
