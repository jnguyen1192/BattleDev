# *******
# * Read input from STDIN
# * Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
# * Use: sys.stderr.write() to display debugging information to STDERR
# * ***/
import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

nb_couleurs = int(lines[0])
couleur_primaires = [2, 3, 5, 7, 11]
minimum_couleur_primaires = set()

for code_couleur in lines[1:]:
    for nb_primaire in couleur_primaires:
        if int(code_couleur) % nb_primaire == 0:
            minimum_couleur_primaires.add(nb_primaire)
my_list = list(minimum_couleur_primaires)
my_list.sort()
my_list = [str(i) for i in my_list]
print(' '.join(my_list))
