import sys
import re
from os import path
from os import mkdir

HERE = path.abspath(path.dirname(__file__))
S1_ROOT_DIR = path.dirname(HERE)
OUTPUT_PATH = path.join(S1_ROOT_DIR, "data/risk_factor_data")

#check to make sure we have a directory to put the output in
if not path.isdir(OUTPUT_PATH):
    mkdir(OUTPUT_PATH)

def detag(text):
    regex = re.compile(r'<.*?>')
    regex_tag_containing_newline = re.compile(r'<.*?\n.*?>')

    text = regex.sub(' ', text)
    text = regex_tag_containing_newline.sub(' ', text)

    return text

def remove_bad_chars(text):
    regex = re.compile(r'&nbsp;')
    return regex.sub(' ', text)

def extract_risk_factors(text):
    regex = re.compile(r'RISK FACTORS[\S\s]*?SPECIAL NOTE REGARDING FORWARD[- ]LOOKING STATEMENTS')

    match = regex.search(text)

    if match:
        filename = sys.argv[1].rstrip('_S-1.txt') + '_risk_factors.txt'
        with open(path.join(OUTPUT_PATH, filename), 'w') as w:
            w.write(match.group())
            w.close()


r = open(sys.argv[1], 'r')

whole_doc = r.read()
whole_doc = detag(whole_doc)
whole_doc = remove_bad_chars(whole_doc)
extract_risk_factors(whole_doc)

r.close()
