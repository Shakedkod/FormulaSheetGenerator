from logic.latex_constants import BASE_LATEX_DOC_END, BASE_LATEX_DOC_START, BASE_LATEX_MATH, BASE_LATEX_PAGE_LAYOUT, BASE_LATEX_TEXT, BASIC_LATEX_MISC, EXTRA_LATEX_PACKAGES_HEADER, LATEX_CODEBLOCK_SETUP, LATEX_HEBREW_TEXT, LATEX_IMAGES_AND_DIAGRAMS, LATEX_TABLE_OF_CONTENTS, LATEX_THEME_REGULAR, LATEX_THEME_REGULAR_HEBREW, LATEX_TIKZ, START_OF_DOCUMENT_CONTENT
from datetime import date, datetime
from pyluach import dates
from pyluach.gematria import gematria

from logic.ast_to_latex import second_pass_parse, parse_ast_to_latex

DEFAULT_LANGUAGE = "english"
DEFAULT_THEME = "regular"
DEFAULT_FOOTER = "\\fancyfoot[C]{\\thepage/\\pageref{LastPage}}"

hebrew_months = {
    1: "ינואר", 2: "פברואר", 3: "מרץ", 4: "אפריל", 
    5: "מאי", 6: "יוני", 7: "יולי", 8: "אוגוסט", 
    9: "ספטמבר", 10: "אוקטובר", 11: "נובמבר", 12: "דצמבר"
}

class LatexFile:
    def __init__(self, preamble: str = "", theme: str = DEFAULT_THEME, language: str = DEFAULT_LANGUAGE, author: str = "", title: str = "", doc_date: str = "", toc: bool = True):
        self.preamble = preamble
        self.language = language
        self.head = {
            "packages": [],
            "tikz": False,
            "code": False,
            "images": False,
            "other": "",
            "has-date": True,
            "has-author": True,
            "extra_lang": []
        }
        
        self.body = ""
        self.header = ""
        self.footer = DEFAULT_FOOTER
        self.table_of_contents = True
        self.theme = theme
        self.author = author
        self.title = title
        self.toc = toc
        
        if doc_date == "":
            today = date.today()
            if language == "hebrew":
                standard_hebrew_date = f"{hebrew_months[today.month]} {today.day}, {today.year}"
                heb_date = dates.HebrewDate.from_gregorian(today)
                day_in_letters = gematria(heb_date.day)
                month_name = heb_date.month_name(hebrew=True)
                year_in_letters = gematria(heb_date.year - 5000)
                traditional_hebrew_date = f"{day_in_letters} ב{month_name} ה'{year_in_letters}"
                self.date = f"{standard_hebrew_date} ({traditional_hebrew_date})"
            else:
                self.date = today.strftime("%B %d, %Y")
        else:
            self.date = doc_date
    
    def add_to_head(self, content: str):
        self.head["other"] += content + "\n"
    
    def enable_tikz(self):
        self.head["tikz"] = True
    
    def add_to_body(self, content: str):
        self.body += content + "\n"
    
    def add_packages(self, packages: list[str]):
        self.head["packages"].extend(packages)
    
    def md_to_latex(self, ast: dict):
        body, self.head = parse_ast_to_latex(ast, self.preamble, self.head)
        body = second_pass_parse(body)
        self.body += body
    
    def add_hebrew_date_to_date(self, date_pattern: str = "%B %d, %Y"):
        today = datetime.strptime(self.date, date_pattern).date()
        heb_date = dates.HebrewDate.from_gregorian(today)
        day_in_letters = gematria(heb_date.day)
        month_name = heb_date.month_name(hebrew=True)
        year_in_letters = gematria(heb_date.year - 5000)
        traditional_hebrew_date = f"{day_in_letters} ב{month_name} ה'{year_in_letters}"
        self.date += f" ({traditional_hebrew_date})"
    
    def add_header(self, header: str):
        self.header += header + "\n"
    
    def delete_header(self):
        self.header = ""
    
    def add_footer(self, footer: str):
        self.footer += footer + "\n"
    
    def delete_footer(self):
        self.footer = ""
    
    def default_footer(self):
        self.footer = DEFAULT_FOOTER
    
    def head_to_text(self) -> str:
        def extra_packages() -> str:
            result = EXTRA_LATEX_PACKAGES_HEADER
            for package in self.head["packages"]:
                result += f"\\usepackage{{{package}}}\n"
            return result
        
        head_text: str = BASE_LATEX_TEXT
        if self.language == "hebrew" or "hebrew" in self.head["extra_lang"]:
            head_text += LATEX_HEBREW_TEXT
        
        head_text += BASE_LATEX_MATH
        if (self.footer != DEFAULT_FOOTER or self.header != ""):
            head_text += BASE_LATEX_PAGE_LAYOUT
            head_text += self.header + "\n" + self.footer + "\n"
        if (self.head["images"] or self.head["tikz"]):
            head_text += LATEX_IMAGES_AND_DIAGRAMS
        if (self.head["tikz"]):
            head_text += LATEX_TIKZ
        
        head_text += BASIC_LATEX_MISC
        head_text += extra_packages()
        
        if self.preamble:
            head_text += "---------- Custom Preamble ----------" + "\n"
            head_text += self.preamble + "\n"
        
        if self.theme == "fancy-academic":
            pass #!WOW - FIX THAT
        else:
            if self.language == "hebrew":
                head_text += LATEX_THEME_REGULAR_HEBREW
            else:
                head_text += LATEX_THEME_REGULAR
        
        if self.head["code"]:
            head_text += LATEX_CODEBLOCK_SETUP
        
        head_text += self.head["other"]
        head_text += "---------- Metadata ----------" + "\n"
        head_text += f"\\title{{{self.title}}}\n"
        head_text += f"\\author{{{self.author}}}\n"
        if self.head["has-date"]:
            head_text += f"\\date{{{self.date}}}\n"
        else:
            head_text += "\\date{}\n"
        
        return head_text
    
    def build(self) -> str:
        document = BASE_LATEX_DOC_START + "\n"
        document += self.head_to_text() + "\n"
        document += START_OF_DOCUMENT_CONTENT + "\n"
        if self.toc:
            document += LATEX_TABLE_OF_CONTENTS + "\n"
        document += self.body + "\n"
        document += BASE_LATEX_DOC_END
        return document