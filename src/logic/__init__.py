DEFAULT_LANGUAGE = "english"
DEFAULT_THEME = "regular"

class LatexFile:
    def __init__(self, preamble: str = None, theme: str = DEFAULT_THEME):
        self.preamble = preamble
        self.language = DEFAULT_LANGUAGE
        self.head = ""
        self.body = ""
        self.header = ""
        self.footer = ""
        self.table_of_contents = True
        self.theme = theme
    
    def add_to_head(self, content: str):
        self.head += content + "\n"
    
    def add_to_head(self, things: dict):
        pass
    
    def add_to_body(self, content: str):
        self.body += content + "\n"
    
    def add_packages(self, packages: list[str]):
        packages_str = "".join([f"{pkg}, " for pkg in packages]).removesuffix(", ")
        self.head += f"\\usepackage{{{packages_str}}}\n"
    
    def md_to_latex(self, ast: dict):
        from logic.ast_to_latex import parse_ast_to_latex
        body, new_head = parse_ast_to_latex(ast, self.preamble)
        
        self.body += body
        self.add_to_head(new_head)
    
    def add_header(self, header: str):
        self.header += header + "\n"
    
    def delete_header(self):
        self.header = ""
    
    def add_footer(self, footer: str):
        self.footer += footer + "\n"
    
    def delete_footer(self):
        self.footer = ""
    
    def default_footer(self):
        self.footer = "\\fancyfoot[C]{\\thepage/\\pageref{LastPage}}"
    
    def build(self) -> str:
        document = BASE_LATEX_DOC_START + "\n"
        document += self.head + "\n"
        document += START_OF_DOCUMENT_CONTENT + "\n"
        document += self.header + "\n"
        document += self.body + "\n"
        document += self.footer + "\n"
        document += BASE_LATEX_DOC_END
        return document