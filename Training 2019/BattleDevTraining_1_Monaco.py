# *******
# * Read input from STDIN
# * Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
# * Use: sys.stderr.write() to display debugging information to STDERR
# * ***/
import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

pos_init = int(lines[0])
nb_evnmt = int(lines[1])

sys.stderr.write("\n" + str(pos_init) + "\n")
sys.stderr.write(str(nb_evnmt) + "\n")
classement = {}
for i in range(1, 21):
    classement[i] = i

sys.stderr.write("\n\n")
for i in classement:
    sys.stderr.write(i + " " + classement[i] + "\n")
sys.stderr.write("\n\n")


def run(pos_init, nb_evnmt):
    cur_pos = pos_init
    for i in range(2, nb_evnmt + 2):
        evnmt = lines[i].split(" ")
        cur_pil = int(evnmt[0])
        e = evnmt[1]
        sys.stderr.write(str(cur_pil) + " " + e + "\n")
        if e == "D" and cur_pos == cur_pil:
            cur_pos -= 1
        elif e == "D" and cur_pos == cur_pil + 1:
            cur_pos += 1
        # +1 pilote concerné
        elif e == "I":
            if pos_init == cur_pil:
                print("KO")
                return 0
            elif pos_init > cur_pil:
                cur_pos -= 1
    # +1 tous les pilotes sauf le pilote concerné
    print(cur_pos)


run(pos_init, nb_evnmt)