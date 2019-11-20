# *******
# * Read input from STDIN
# * Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
# * Use: sys.stderr.write() to display debugging information to STDERR
# * ***/
import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

nb_enfant = int(lines[0])
age_enfants = lines[1]

nb_enfants_tobogan = 0

for i in age_enfants.split(" "):
    if int(i) >= 5 and int(i) <= 9:
        nb_enfants_tobogan += 1

print(nb_enfants_tobogan)