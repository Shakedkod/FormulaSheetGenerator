import copy

from logic.obsidian_special_blocks import obsidian_link, self_ref

def get_text(children: list, head: dict = {}) -> tuple[str, dict]:
    """
    Recursively extracts text from a list of children nodes.
    """
    text = ""
    for child in children:
        # normal text and text looking
        if child["type"] == "text":
            text += child["raw"]
        elif child["type"] == "strong":
            bold_text, head = get_text(child.get("children", []), head)
            text += bold(bold_text)
        elif child["type"] == "emphasis":
            italic_text, head = get_text(child.get("children", []), head)
            text += emph(italic_text)
        elif child["type"] == "underline":
            underline_text, head = get_text(child.get("children", []), head)
            text += underline(underline_text)
        elif child["type"] == "thematic_break":
            text += thematic_break()
        # math
        elif child["type"] == "inline_math":
            text += math_inline(child["raw"])
        
        # links & references
        elif child["type"] == "link":
            link_text, head = get_text(child.get("children", []), head)
            link_url = child.get("attrs", {}).get("href", "")
            text += link(link_text, link_url)
        elif child["type"] == "wiki_link":
            link_text = child.get("raw", "")
            link_url = child.get("attrs", {}).get("link", "")
            
            if link_url.startswith("#") or link_url.startswith("^"):
                if link_url.startswith("#"):
                    link_url = link_url[link_url.find("^"):]
                text += self_ref(link_url[1:], link_text)
            else:
                heading = child.get("attrs", {}).get("heading", "")
                block_ref = child.get("attrs", {}).get("block_ref", "")
                if block_ref:
                    ref = f"{block_ref}"
                elif heading:
                    ref = f"{heading}"
                else:
                    ref = ""
                text += obsidian_link(link_text, link_url, ref)
        
        # line breaks
        elif child["type"] == "linebreak":
            text += newline()
        
        # lists, images, and other elements
        elif child["type"] == "list":
            text += parse_list(child)
        elif child["type"] == "image":
            head["images"] = True
            image_path = child.get("attrs", {}).get("src", "")
            text += image(image_path)
        elif child["type"] == "wiki_embed":
            embed_path = child.get("attrs", {}).get("link", "") + ".svg"
            size = child.get("attrs", {}).get("size", "0.8\\textwidth")
            text += svg(embed_path, size)
        elif child["type"] == "svg":
            head["images"] = True
            svg_path = child.get("attrs", {}).get("src", "")
            text += svg(svg_path)
        elif "children" in child:
            text, head = get_text(child["children"], head)
        else:
            text += ""
    return (text, head)

def get_header(header: dict) -> str:
    level = header.get("attrs", {}).get("level", 1)
    title, _ = get_text(header.get("children", []))
    if level == 1:
        return h1(title)
    elif level == 2:
        return h2(title)
    elif level == 3:
        return h3(title)
    elif level == 4:
        return h4(title)
    elif level == 5:
        return h5(title)
    else:
        return h6(title)

def h1(title: str) -> str:
    return f"\\part{{{title}}}\n"

def h2(title: str) -> str:
    return f"\\section{{{title}}}\n"

def h3(title: str) -> str:
    return f"\\subsection{{{title}}}\n"

def h4(title: str) -> str:
    return f"\\subsubsection{{{title}}}\n"

def h5(title: str) -> str:
    return f"\\paragraph{{{title}}}\n"

def h6(title: str) -> str:
    return f"\\subparagraph{{{title}}}\n"

def bold(text: str) -> str:
    return f"\\textbf{{{text}}}"

def emph(text: str) -> str:
    return f"\\emph{{{text}}}"

def underline(text: str) -> str:
    return f"\\underline{{{text}}}"

def blank_line() -> str:
    return "" #"\\vspace{{{1}\\baselineskip}}\n"

def mathText(text: str) -> str:
    return text.replace("\\R", "").replace("\\begin{align}", "\\begin{aligned}").replace("\\end{align}", "\\end{aligned}").replace("\\begin{align*}", "\\begin{aligned}").replace("\\end{align*}", "\\end{aligned}").replace("\\Large", "\\Big")

def math_inline(text: str) -> str:
    return f"\\({{{mathText(text)}}}\\)"

def math_block(text: str) -> str:
    return f"\\[\n{{{mathText(text)}}}\n\\]\n"

def newline() -> str:
    return "\\newline{}\n"

def link(text: str, url: str) -> str:
    return f"\\href{{{url}}}{{{text}}}"

def image(path: str, width: str = "0.8\\textwidth") -> str:
    return f"\\begin{{figure}}[h!]\n\\centering\n\\includegraphics[width={width}]{{{path}}}\n\\end{{figure}}\n"

def svg(path: str, width: str = "0.8\\textwidth") -> str:
    return f"\\begin{{figure}}[h!]\n\\centering\n\\includesvg[width={width}]{{{path}}}\n\\end{{figure}}\n"

def thematic_break() -> str:
    return "\\hrulefill\n"

def table(table_content: dict) -> str:
    """
    Converts a table represented as a dictionary to LaTeX tabular format.
    """
    result = "\\begin{table}[h]\n\\centering\n"
    result += "\\begin{tabular}{|"
    
    # Determine the column alignment based on the first row of the table
    if "children" in table_content and len(table_content["children"]) > 0:
        first_row = table_content["children"][0]
        if "children" in first_row:
            for cell in first_row["children"]:
                align = cell.get("attrs", {}).get("align", "left")
                if align == "center":
                    result += "c|"
                elif align == "right":
                    result += "r|"
                else:
                    result += "l|"
    
    result += "}\n"
    
    # Process table head
    for child in table_content.get("children", []):
        if child["type"] == "table_head":
            for row in child.get("children", []):
                if row["type"] == "table_row":
                    row_content = []
                    for cell in row.get("children", []):
                        cell_content = ""
                        for cell_child in cell.get("children", []):
                            if cell_child["type"] == "text":
                                cell_content += cell_child["raw"]
                            elif cell_child["type"] == "inline_math":
                                cell_content += math_inline(cell_child["raw"])
                        row_content.append(cell_content)
                    result += " & ".join(row_content) + " \\\\\n"
                    result += "\\hline\n"
            result += "\\hline\n"

    # Process table body
    for child in table_content.get("children", []):
        if child["type"] == "table_body":
            for row in child.get("children", []):
                if row["type"] == "table_row":
                    row_content = []
                    for cell in row.get("children", []):
                        cell_content = ""
                        for cell_child in cell.get("children", []):
                            if cell_child["type"] == "text":
                                cell_content += cell_child["raw"]
                            elif cell_child["type"] == "inline_math":
                                cell_content += math_inline(cell_child["raw"])
                        row_content.append(cell_content)
                    result += " & ".join(row_content) + " \\\\\n"
                    result += "\\hline\n"
    
    result += "\\end{tabular}\n\\end{table}\n"
    return result

def list_content_parse(list_content: dict) -> str:
    result = ""
    
    for item in list_content:
            if item["type"] == "list_item":
                item_text, _ = get_text(item.get("children", []))
                result += f"\\item {item_text}\n"
                
    return result

def enumerate(list_content: dict) -> str:
    result = "\\begin{enumerate}\n"
    result += list_content_parse(list_content)
    return result + "\\end{enumerate}\n"

def itemize(list_content: dict) -> str:
    result = "\\begin{itemize}\n"
    result += list_content_parse(list_content)
    return result + "\\end{itemize}\n"

def parse_list(list: dict) -> str:
    """
    Converts a list represented as a dictionary to LaTeX itemize or enumerate format.
    """
    props = copy.deepcopy(list)
    props.pop("children")
    props.pop("type")
    
    if (props["attrs"]["ordered"]):
        return enumerate(list["children"])
    else:
        return itemize(list["children"])