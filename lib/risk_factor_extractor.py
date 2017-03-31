import re
import sys

r = open(sys.argv[1], 'r')

regex = re.compile(r'RISK FACTORS[\S\s]*?SPECIAL NOTE REGARDING FORWARD[- ]LOOKING STATEMENTS')

match = regex.search(r.read())

if match:
    with open(sys.argv[1] + '_risk_factors.txt', 'w') as w:
        w.write(match.group())
        w.close()

r.close()
