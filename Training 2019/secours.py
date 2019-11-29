# *******
# * Read input from STDIN
# * Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
# * Use: sys.stderr.write() to display debugging information to STDERR
# * ***/
import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

aller_retour = 0
nb_bateaux_panne = lines[0]

# secours = 10 personnes et un bateau a la fois
for nb_voyageur_par_bateau in lines[1:]:
    # print(int(nb_voyageur_par_bateau))
    nb_pass_a_secourir = int(nb_voyageur_par_bateau)
    while nb_pass_a_secourir > 0:
        nb_pass_a_secourir -= 10
        aller_retour += 1
print(aller_retour)
