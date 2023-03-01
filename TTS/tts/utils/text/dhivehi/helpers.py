
import re
from unidecode import unidecode

_rufiyaa_re = re.compile(r"(?<=\d)ރ")

_suffixes = {
    "ދޭށެވެ" : "ދޭން",
    "ޑެވެ" : "ޑު",
    "ށެވެ" : "ށް",
    "ންނެވެ" : "ން",
    "ނެވެ" : "ން",
    "ކެވެ" : "އް",
    "މެވެ" : "ން" ,
    "ތެވެ" : "ތް",
    "ހެވެ" : "ސް",
    "ގެވެ": "ގު",
    "ންޏެވެ": "ންޏޭ",
    "ކަ އެވެ": "ކާ",
    "ނެ އެވެ": "ނޭ",
    "ވެ އެވެ": "ވޭ",
    "ދެ އެވެ": "ދޭ",
    "ގަ އެވެ": "ގައި",
    "ރެ އެވެ": "ރޭ",
    "ކެވެ": "އް",
    "ވި އެވެ": "ވި",
    "އެވެ" : "",
     "ގެވެ": "ގެ"   
}
  

# Arabic formulas and ligatures
ARABIC_GRAPHEMES = [
    (re.compile(r"\sﷲ\s"), "އައްލޯހު"),
    (re.compile(r"\bﷲ"), "އުއްލޯ"),
    (re.compile("ﷺ"), "ޞައްލައްލޯހު އަލައިހި ވަސައްލަމް"),
    (re.compile("صلى الله عليه و سلم"), "ޞައްލައްލޯހު އަލައިހި ވަސައްލަމް"),
    (re.compile("عليه السلام"), "ޢަލައިހިއްސަލާމް")
]

# Alphabets and their corresponding sounds
DHIVEHI_ALPHABETS = [
    (re.compile(r"ޑރ\.\s?"), " ޑޮކްޓަރު"),
    (re.compile(r"އއ\.\s?"), " އަލިފު އަލިފު"),
    (re.compile(r"އދ\.\s?"), " އަލިފުދާލު"),
    (re.compile(r"ކ\.\s?"), " ކާފު"),
    (re.compile(r"ހއ\.\s?"), " ހާއަލިފު"),
    (re.compile(r"ހދ\.\s?"), " ހާދާލު"),
    (re.compile(r"ށ\.\s?"), " ޝަވިޔަނި"),
    (re.compile(r"ނ\.\s?"), " ނޫނު"),
    (re.compile(r"ރ\.\s?"), " ރާ"),
    (re.compile(r"ބ\.\s?"), " ބާ"),
    (re.compile(r"ޅ\.\s?"), " ޅަވިޔަނި"),
    (re.compile(r"ފ\.\s?"), " ފާފު"),
    (re.compile(r"ވ\.\s?"), " ވާވު"),
    (re.compile(r"މ\.\s?"), " މީމު"),
    (re.compile(r"ދ\.\s?"), " ދާލު"),
    (re.compile(r"ތ\.\s?"), " ތާ"),
    (re.compile(r"ލ\.\s?"), " ލާމު"),
    (re.compile(r"ގއ\.\s?"), " ގާފުއަލިފު"),
    (re.compile(r"ގދ\.\s?"), " ގާފުދާލު"),
    (re.compile(r"ޏ\.\s?"), " ޏަވިޔަނި")
]


def expand_ar_graphemes(text):
    for regex, replacement in ARABIC_GRAPHEMES:
        text = re.sub(regex, replacement, text)
    return text


def expand_dv_abbreviations(text):
    for regex, replacement in DHIVEHI_ALPHABETS:
        text = re.sub(regex, replacement, text)
    return text

def _perform_decimal_number_expansion(match_obj):
    res = ""
    point = match_obj.string[match_obj.span()[0]] 
    
    if point is not None and point == ".":
        res += " ޕޮއިންޓު "
    for i in range(match_obj.span()[0] + 1, match_obj.span()[1]):
        res += match_obj.string[i] + " "
    return res

def expand_post_decimal_numbers(text):
    return re.sub(r"\.\d+\b", _perform_decimal_number_expansion, text)
    
def clean_long_numbers(text):
    return re.sub(r"(\d+),(\d+)", r"\1\2", text)

def clean_numbers(text):
    text = clean_long_numbers(text)
    text = expand_post_decimal_numbers(text)
    return text

def expand_rufiyaa(text):
    return re.sub(_rufiyaa_re, " ރުފިޔާ ", text)

def convert_dv_to_ascii(text):
    return unidecode(text)

def remove_dhivehi_suffixes(text):
    for key, value in _suffixes.items():
        text = text.replace(key, value)
    return text