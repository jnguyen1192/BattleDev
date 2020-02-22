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
        p_generic = []
        for pierre in pierres:
            p_generic.append([pierre[0] / pierre[1], pierre[0], pierre[1]])
        for poudre in poudres:
            for _ in range(poudre[1]):
                p_generic.append([poudre[0], poudre[0], 1])
        return sorted(p_generic, reverse=True)

    def get_total(self):
        capacite = self.capacite
        dollar = 0
        for p in self.p_generic:
            capacite -= p[2]
            if capacite < 0:
                break
            dollar += p[1]
        if capacite != -1:
        # cas ou il faut maximiser

        return dollar


elmts = elements(valeur_pierres, valeur_poudres, C)
sys.stderr.write(str(elmts.pierres))
sys.stderr.write(str(elmts.poudres))
sys.stderr.write(str(elmts.p_generic))
print(str(elmts.total))




