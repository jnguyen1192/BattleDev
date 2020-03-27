# *******
# * Read input from STDIN
# * Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
# * Use: sys.stderr.write() to display debugging information to STDERR
# * ***/
import sys

f = open("input.txt")

lines = []
for line in f:#sys.stdin:
    lines.append(line.rstrip('\n'))
f.close()


print(lines)

