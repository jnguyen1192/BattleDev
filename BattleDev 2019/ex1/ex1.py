# *******
# * Read input from STDIN
# * Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
# * Use: sys.stderr.write() to display debugging information to STDERR
# * ***/
import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

nb_participant = int(lines[0])

long_min = 1001

sans_tente = ""

for participant in lines[1:]:
    prenom_longueur_bout_de_bois = participant.split(" ")
    prenom = prenom_longueur_bout_de_bois[0]
    longueur_bout_de_bois = int(prenom_longueur_bout_de_bois[1])
    if longueur_bout_de_bois < long_min:
        sans_tente = prenom
        long_min = longueur_bout_de_bois

print(sans_tente)