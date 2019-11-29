# *******
# * Read input from STDIN
# * Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
# * Use: sys.stderr.write() to display debugging information to STDERR
# * ***/
import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

nb_ligne_nb_station_str = lines[0].split(" ")

N = int(nb_ligne_nb_station_str[0])
M = int(nb_ligne_nb_station_str[1])

num_dep_num_arr_str = lines[1].split(" ")

num_dep = int(num_dep_num_arr_str[0])
num_arr = int(num_dep_num_arr_str[1])

nb_station_par_ligne = [int(str_) for str_ in lines[2].split(" ")]

num = 1
station_dict = {}
ligne_dict = {}
station_couple = []
lignes = []

# construction des noeuds de l'arbre ligne_dict avec ses fils
for l in lines[3:]:
    # affecter a chaque station la/les ligne(s) disponible
    for station in [int(str_) for str_ in l.split(" ")]:
        try:
            station_dict[station].add(num)
        except KeyError:
            # print("KeyError encountered")
            station_dict[station] = set()
        station_dict[station].add(num)
        # affecter a chaque ligne, les lignes accessibles
        try:
            ligne_dict[num] = ligne_dict[num].union(station_dict[station])
        except KeyError:
            # print("KeyError encountered")
            ligne_dict[num] = set()
        ligne_dict[num] = ligne_dict[num].union(station_dict[station])
    num += 1

# affecter aux anciennes lignes, les nouvelles lignes en liaison
for n in range(num - 1, 0, -1):
    for l in ligne_dict[n]:
        ligne_dict[l].add(n)

ligne_arr = list(station_dict[num_arr])[0]
ligne_dep = list(station_dict[num_dep])[0]
# cas egale
if station_dict[num_dep] == station_dict[num_arr] or station_dict[num_dep].issubset(station_dict[num_arr]) or \
        station_dict[num_arr].issubset(station_dict[num_dep]):
    print("1")
# cas impossible
elif len(ligne_dict[ligne_dep]) == 1 and len(ligne_dict[ligne_arr]) == 1:
    print(-1)
else:
    # case ligne du debut
    lignes_du_debut = ligne_dict[ligne_dep]
    incr_deb = 2
    end = False
    inter_lignes = []
    while not end:
        if incr_deb > N:
            break
        for ligne in lignes_du_debut:
            if ligne_arr == ligne:
                lignes_du_debut = []
                end = True
                break
            inter_lignes += ligne_dict[ligne]
        if end == True:
            break
        lignes_du_debut = inter_lignes
        inter_lignes = []
        incr_deb += 1
    # cas ligne de fin
    lignes_de_fin = ligne_dict[ligne_arr]
    incr_fin = 2
    end = False
    inter_lignes = []
    while not end:
        if incr_fin > N:
            break
        for ligne in lignes_de_fin:
            if ligne_dep == ligne:
                lignes_de_fin = []
                end = True
                break
            inter_lignes += ligne_dict[ligne]
        if end == True:
            break
        lignes_de_fin = inter_lignes
        inter_lignes = []
        incr_fin += 1
    if incr_fin == N + 1 and incr_deb == N + 1:
        print(-1)
    elif incr_fin > incr_deb:
        print(incr_deb)
    else:
        print(incr_fin)
