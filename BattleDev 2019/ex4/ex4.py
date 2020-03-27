# *******
# * Read input from STDIN
# * Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
# * Use: sys.stderr.write() to display debugging information to STDERR
# * ***/
import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))
    sys.stderr.write(line.rstrip('\n') + "\n")

N, M, C = [int(i) for i in lines[0].split(" ")]
sys.stderr.write(str(N) + " " + "\n")
valeur_pierres = [list(map(int, l.split(" "))) for l in lines[1:N + 1]]
valeur_poudres = [list(map(int, l.split(" "))) for l in lines[N + 1:]]


class elements:
    def __init__(self, pierres, poudres, capacite):
        self.pierres = pierres
        self.poudres = poudres
        self.p_generic = self.get_p_generic(pierres, poudres)
        self.capacite = capacite
        self.total = self.get_total()

    def get_p_generic(self, pierres, poudres):
        # on ordonne les valeurs de pierres et de poudres par ordre décroissant avec comme identifiant dollars/gramme
        p_generic = []
        for pierre in pierres:
            p_generic.append([pierre[0] / pierre[1], pierre[0], pierre[1]])
        for poudre in poudres:
            for _ in range(poudre[1]):
                p_generic.append([poudre[0], poudre[0], 1])
        return sorted(p_generic, reverse=True)

    def process_total(self):
        # le process consiste a parcourir la liste des pierres/poudres ordonnées et a les ajouter dans le sac au fur et à mesure, si le sac déborde, on ignore la pierre ou la poudre correspondante
        capacite = self.capacite
        dollar  = 0
        # on enregistre une variable pour rollback
        old_capacite = capacite
        for p in self.p_generic:
            capacite -= p[2]
            # on soustrait la capacite
            if capacite == 0:
                # cas final, en ajoutant le montant
                dollar += p[1]
                break
            elif capacite < 0:
                # cas ou la capacite est négative, on utilise le rollback
                capacite = old_capacite
                dollar -= p[1]
            # cas normal, on ajoute le montant
            dollar += p[1]
            # on fait un commit
            old_capacite = capacite
        return dollar, capacite

    def get_total(self):
        total, capacite = self.process_total()
        return total


elmts = elements(valeur_pierres, valeur_poudres, C)
sys.stderr.write(str(elmts.pierres))
sys.stderr.write(str(elmts.poudres))
sys.stderr.write(str(elmts.total) + "\n")
print(str(elmts.total))




