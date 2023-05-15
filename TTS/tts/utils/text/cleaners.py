# -*- coding: utf-8 -*-
# Copyright (c) 2017 Keith Ito
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import re
from dhivehi.numbers_to_thaana_transliterator import NumbersToThaanaTransliterator
from unidecode import unidecode

# numbers transliterator
transliterator = NumbersToThaanaTransliterator()

_rufiyaa_re = re.compile(r"(?<=\d)ރ")

# Regular expression matching whitespace:
_whitespace_re = re.compile(r"\s+")

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
    (re.compile(r"ޑރ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " ޑޮކްޓަރު"),
    (re.compile(r"އއ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " އަލިފު އަލިފު"),
    (re.compile(r"އދ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " އަލިފުދާލު"),
    (re.compile(r"ކ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " ކާފު"),
    (re.compile(r"ހ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), "ހާ "),
    (re.compile(r"ހއ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " ހާއަލިފު"),
    (re.compile(r"ހދ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " ހާދާލު"),
    (re.compile(r"ށ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " ޝަވިޔަނި"),
    (re.compile(r"ނ(?![ްެޭުޫިީަާޮޯ])[\.\s\)\(]+"), " ނޫނު"),
    (re.compile(r"ރ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " ރާ"),
    (re.compile(r"ބ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " ބާ"),
    (re.compile(r"ޅ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " ޅަވިޔަނި"),
    (re.compile(r"ފ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " ފާފު"),
    (re.compile(r"ވ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " ވާވު"),
    (re.compile(r"މ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " މީމު"),
    (re.compile(r"ދ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " ދާލު"),
    (re.compile(r"ތ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " ތާ"),
    (re.compile(r"ލ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " ލާމު"),
    (re.compile(r"ގއ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " ގާފުއަލިފު"),
    (re.compile(r"ގދ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " ގާފުދާލު"),
    (re.compile(r"ޏ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " ޏަވިޔަނި"),
    (re.compile(r"ގ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " ގާފު"),
    (re.compile(r"ޖ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " ޖަވިޔަނި"),
    (re.compile(r"ޑރ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " ޑޮކްޓަރު"),
    (re.compile(r"ޑ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " ޑަވިޔަނި"),
    (re.compile(r"ޗ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " ޗަވިޔަނި"),
    (re.compile(r"ޓ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " ޓަވިޔަނި"),
    (re.compile(r"ޕ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " ޕަވިޔަނި"),
    (re.compile(r"ޔ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " ޔާ"),
    (re.compile(r"ޝ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " ޝީނު"),
    (re.compile(r"ޒ(?![ްެޭުޫިީަާޮޯ])[\.\s]?"), " ޒަވިޔަނި"),
]

# List of (regular expression, replacement) pairs for abbreviations:
_abbreviations = [
    (re.compile("\\b%s\\." % x[0], re.IGNORECASE), x[1])
    for x in [
        ("mrs", "misess"),
        ("mr", "mister"),
        ("dr", "doctor"),
        ("st", "saint"),
        ("co", "company"),
        ("jr", "junior"),
        ("maj", "major"),
        ("gen", "general"),
        ("drs", "doctors"),
        ("rev", "reverend"),
        ("lt", "lieutenant"),
        ("hon", "honorable"),
        ("sgt", "sergeant"),
        ("capt", "captain"),
        ("esq", "esquire"),
        ("ltd", "limited"),
        ("col", "colonel"),
        ("ft", "fort"),
    ]
]

def expand_ar_graphemes(text):
    for regex, replacement in ARABIC_GRAPHEMES:
        text = re.sub(regex, replacement, text)
    return text


def expand_dv_abbreviations(text):
    for regex, replacement in DHIVEHI_ALPHABETS:
        text = re.sub(regex, replacement, text)
    return text


def expand_abbreviations(text):
    for regex, replacement in _abbreviations:
        text = re.sub(regex, replacement, text)
    return text


def lowercase(text):
    return text.lower()

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

def collapse_whitespace(text):
    return re.sub(_whitespace_re, " ", text)


def convert_to_ascii(text):
    return unidecode(text)


def basic_cleaners(text):
    """Basic pipeline that lowercases and collapses whitespace without transliteration."""
    text = lowercase(text)
    text = collapse_whitespace(text)
    return text


def remove_dhivehi_suffixes(text):
    for key, value in _suffixes.items():
        text = text.replace(key, value)
    return text
    

def dhivehi_cleaners(text):
    text = expand_rufiyaa(text)
    text = clean_numbers(text)
    text = transliterator.transliterate_text(text)
    # we should not remove dhivehi suffixes
    # text = remove_dhivehi_suffixes(text)
    text = expand_dv_abbreviations(text)
    text = expand_ar_graphemes(text)
    text = convert_to_ascii(text)
    text = lowercase(text)
    text = collapse_whitespace(text)
    return text
