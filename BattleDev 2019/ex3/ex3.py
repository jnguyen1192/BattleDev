# *******
# * Read input from STDIN
# * Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
# * Use: sys.stderr.write() to display debugging information to STDERR
# * ***/
import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

cables_requetes = lines[0].split(" ")
sys.stderr.write(cables_requetes[0] + " " + cables_requetes[1] + "\n")
cables = int(cables_requetes[0])
requetes = int(cables_requetes[1])

durees = []
for i_d, d in enumerate(lines[2:]):
    tmp = [int(p) for p in d.split(" ")]
    tmp_ = (tmp[0], tmp[1], i_d + 1)
    durees.append(tmp_)

# sys.stderr.write("Non triee\n")
# for d in durees:
#    sys.stderr.write(str(d[0]) + " " + str(d[1]) + " " + str(d[2]) + "\n")
durees = sorted(durees)

# sys.stderr.write("Triee\n")
# for d in durees:
#    sys.stderr.write(str(d[0]) + " " + str(d[1]) + " " + str(d[2]) + "\n")

cables_disponibles = [(i + 1, 0) for i in range(cables)]
cables_utilisees = []
res_fin = []
sys.stderr.write("\n\n")
error = False
current_nb_cable = cables
old_cable_debut = -1
for d in durees:
    # en fonction la fin des cables utilisees [1], liberer les cables correspondant dans disponible
    for c in cables_utilisees:
        if c[1] < d[0]:
            cables_disponibles.append((c[0], 0))
            cables_disponibles = sorted(cables_disponibles)
            cables_utilisees.remove(c)
    # ajouter un cable a utiliser
    try:
        new_use_cable = (cables_disponibles[0][0], d[1])
        res_fin.append(cables_disponibles[0][0])
        cables_disponibles.pop(0)
    except:
        error = True
        break
    cables_utilisees.append(new_use_cable)
sys.stderr.write("\nLenfin " + str(len(res_fin)) + "\n")

if error:
    print("pas possible")
else:
    if len(res_fin) != requetes:
        res_fin.append(cables_disponibles[0][0])

    print(" ".join(str(i) for i in res_fin))