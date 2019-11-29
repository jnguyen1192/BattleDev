# *******
# * Read input from STDIN
# * Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
# * Use: sys.stderr.write() to display debugging information to STDERR
# * ***/
import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

planches = [int(p) for p in lines]

long_min_planche = min(planches)

long_max = long_min_planche * 4

total = 0
for p in planches:
    total += p

print(total - long_max)