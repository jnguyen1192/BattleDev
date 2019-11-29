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
vp = []
pq = []

for valeur_poids in lines[1:N + 1]:
    tmp_ = [int(i) for i in valeur_poids.split(" ")]
    vp.append((float(float(tmp_[0]) / float(tmp_[1])), tmp_[0], tmp_[1], "v"))

# sys.stderr.write("lennnnnn(vp)" + str(len(vp)) + " " + "\n")
for prixaupoids_quantitedispo in lines[N + 1:]:
    tmp = [int(i) for i in prixaupoids_quantitedispo.split(" ")]
    vp.append((tmp[0], tmp[1], 0, "p"))

# sys.stderr.write("lennnnnn(pq)" + str(len(pq)) + " " + "\n")

vp = sorted(vp, reverse=True)
# sys.stderr.write("poid\n")
for v in vp:
    sys.stderr.write(str(v[0]) + " " + str(v[1]) + " " + str(v[2]) + " " + str(v[3]) + "\n")


# pq = sorted(pq, reverse=True)
# sys.stderr.write("poudre\n")
# for p in pq:
#    sys.stderr.write(str(p[0]) + " " + str(p[1]) + "\n")

def solve(vp, only_p=False):
    dollar = 0
    tot = 0
    vp2 = vp.copy()
    for i_v, v in enumerate(vp):
        # sys.stderr.write(str(tot) + "\n")
        if v[3] == "v" and only_p == False:
            if tot + v[2] <= C:
                dollar += v[1]
                sys.stderr.write("+ " + str(v[1]) + "\n")
                vp2.remove(v)
                tot += v[2]
        else:
            for i in range(v[1]):
                if tot + 1 <= C:
                    tot += 1
                    dollar += v[0]
                    sys.stderr.write("+ " + str(v[0]) + "\n")
                else:
                    break
                # test pierre
                reste = (v[1] - i + 1) * v[0]
                for v2 in vp2:
                    if v2[3] == "v" and tot + v2[2] <= C and reste < v2[1]:
                        dollar += v2[1]
                        sys.stderr.write("+ " + str(v2[1]) + "\n")
                        vp2.remove(v2)
                        tot += v2[2]
    return dollar, tot


vp_2 = vp.copy()
dollar_3, tot_3 = solve(vp, True)
dollar, tot = solve(vp)
sys.stderr.write("dollar_2\n")
try:
    tmp = vp_2[0]
    vp_2[0] = vp_2[1]
    vp_2[1] = vp_2[0]
except:
    pass
dollar_2, tot_2 = solve(vp_2)
if dollar_2 > dollar:
    dollar = dollar_2
    tot = tot_2
if dollar_3 > dollar:
    dollar = dollar_3
    tot = tot_3

print(dollar)

sys.stderr.write("Total = " + str(tot) + " " + "\n")
sys.stderr.write("Dollar = " + str(dollar) + " " + "\n")
