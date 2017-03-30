import sys
import re


def detag(text):
    regex = re.compile(r'<.*?>')
    regex_tag_containing_newline = re.compile(r'<.*?\n.*?>')

    text = regex.sub(' ', text)
    text = regex_tag_containing_newline.sub(' ', text)

    return text

def remove_bad_chars(text):
    regex = re.compile(r'&nbsp;')
    return regex.sub(' ', text)


r = open(sys.argv[1], 'r')
w = open(sys.argv[1] + '_cleaned.txt', 'w')

whole_doc = r.read()
whole_doc = detag(whole_doc)
whole_doc = remove_bad_chars(whole_doc)

w.write(whole_doc)



w.close()
r.close()
