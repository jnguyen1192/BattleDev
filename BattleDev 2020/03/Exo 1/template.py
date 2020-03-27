# *******
# * Read input from STDIN
# * Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
# * Use: sys.stderr.write() to display debugging information to STDERR
# * ***/
import sys
from collections import defaultdict


def leaders(xs, top=10):
    counts = defaultdict(int)
    for x in xs:
        counts[x] += 1
    return sorted(counts.items(), reverse=True, key=lambda tup: tup[1])[:top]


lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

colors = lines[2:]

leads = leaders(colors, 2)
print(leads[0][0], leads[1][0])
