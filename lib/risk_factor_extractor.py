import re
import sys

r = open(sys.argv[1], 'r')
w = open(sys.argv[1] + '_risk_factors.txt', 'w')

regex = re.compile(r'RISK FACTORS[\S\s]*?SPECIAL NOTE REGARDING FORWARD[- ]LOOKING STATEMENTS')

match = regex.search(r.read())
print(match.group())




r.close()
w.close()
