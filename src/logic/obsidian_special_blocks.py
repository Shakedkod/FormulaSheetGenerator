def self_ref(link: str, title: str) -> str:
    """
    Generates a LaTeX refrence to a thing in ths file.
    """
    return f"\\hyperref[{link}]{{{title}}}\n"

def obsidian_link(title: str, url: str, block_ref: str) -> str:
    """
    Generates a LaTeX link for an Obsidian link.
    """
    return f"\\href{{https://uni-folder.vercel.app/{url}#{block_ref}}}{{{title}}}\n"

def quote(text: str, type: str, ref: str = "") -> str:
    """
    Generates a LaTeX quote.
    """
    if ref:
        return f"\\begin{{{type}}}\n\\label{{{ref}}}\n{text}\n\\end{{{type}}}\n"
    return f"\\begin{{{type}}}\n{text}\n\\end{{{type}}}\n"

def titled_quote(text: str, title: str, type: str, ref: str = "") -> str:
    """
    Generates a LaTeX quote with a title.
    """
    if ref:
        return f"\\begin{{{type}}}[{title}]\n\\label{{{ref}}}\n{text}\n\\end{{{type}}}\n"
    return f"\\begin{{{type}}}[{title}]\n{text}\n\\end{{{type}}}\n"

def definition(text: str, title: str = "", ref: str = "") -> str:
    """
    Generates a LaTeX definition.
    """
    if title:
        return titled_quote(text, title, "definition", ref)
    return quote(text, "definition", ref)

def theorem(text: str, title: str = "", ref: str = "") -> str:
    """
    Generates a LaTeX theorem.
    """
    if title:
        return titled_quote(text, title, "theorem", ref)
    return quote(text, "theorem", ref)

def lemma(text: str, title: str = "", ref: str = "") -> str:
    """
    Generates a LaTeX lemma.
    """
    if title:
        return titled_quote(text, title, "lemma", ref)
    return quote(text, "lemma", ref)

def proposition(text: str, title: str = "", ref: str = "") -> str:
    """
    Generates a LaTeX proposition.
    """
    if title:
        return titled_quote(text, title, "proposition", ref)
    return quote(text, "proposition", ref)

def corollary(text: str, title: str = "", ref: str = "") -> str:
    """
    Generates a LaTeX corollary.
    """
    if title:
        return titled_quote(text, title, "corollary", ref)
    return quote(text, "corollary", ref)

def claim(text: str, title: str = "", ref: str = "") -> str:
    """
    Generates a LaTeX claim.
    """
    if title:
        return titled_quote(text, title, "claim", ref)
    return quote(text, "claim", ref)

def conjecture(text: str, title: str = "", ref: str = "") -> str:
    """
    Generates a LaTeX conjecture.
    """
    if title:
        return titled_quote(text, title, "conjecture", ref)
    return quote(text, "conjecture", ref)

def axiom(text: str, title: str = "", ref: str = "") -> str:
    """
    Generates a LaTeX axiom.
    """
    if title:
        return titled_quote(text, title, "axiom", ref)
    return quote(text, "axiom", ref)

def assumption(text: str, title: str = "", ref: str = "") -> str:
    """
    Generates a LaTeX assumption.
    """
    if title:
        return titled_quote(text, title, "assumption", ref)
    return quote(text, "assumption", ref)

def example(text: str, title: str = "", ref: str = "") -> str:
    """
    Generates a LaTeX example.
    """
    if title:
        return titled_quote(text, title, "example", ref)
    return quote(text, "example", ref)

def exercise(text: str, title: str = "", ref: str = "") -> str:
    """
    Generates a LaTeX exercise.
    """
    if title:
        return titled_quote(text, title, "exercise", ref)
    return quote(text, "exercise", ref)

def hypothesis(text: str, title: str = "", ref: str = "") -> str:
    """
    Generates a LaTeX hypothesis.
    """
    if title:
        return titled_quote(text, title, "hypothesis", ref)
    return quote(text, "hypothesis", ref)

def remark(text: str, title: str = "", ref: str = "") -> str:
    """
    Generates a LaTeX remark.
    """
    if title:
        return titled_quote(text, title, "remark", ref)
    return quote(text, "remark", ref)

def hw(text: str, title: str = "", ref: str = "") -> str:
    """
    Generates a LaTeX homework.
    """
    if title:
        return titled_quote(text, title, "hw", ref)
    return quote(text, "hw", ref)

def callout(text: str, attrs: dict) -> str:
    """
    Generates a LaTeX callout.
    """
    title = attrs.get("title", "")
    ref = attrs.get("block_id", "")
    
    match attrs.get("callout_type", "").lower():
        case "definition":
            return definition(text, title, ref)
        case "theorem":
            return theorem(text, title, ref)
        case "lemma":
            return lemma(text, title, ref)
        case "proposition":
            return proposition(text, title, ref)
        case "corollary":
            return corollary(text, title, ref)
        case "claim":
            return claim(text, title, ref)
        case "conjecture":
            return conjecture(text, title, ref)
        case "axiom":
            return axiom(text, title, ref)
        case "assumption":
            return assumption(text, title, ref)
        case "example":
            return example(text, title, ref)
        case "exercise":
            return exercise(text, title, ref)
        case "hypothesis":
            return hypothesis(text, title, ref)
        case "remark":
            return remark(text, title, ref)
        case "hw":
            return hw(text, title, ref)
        case _:
            return quote(text, "quote", ref)
