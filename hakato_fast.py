#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

participants = []
nb_participant = 0

for line in sys.stdin:
    if nb_participant == 0:
        nb_participant = line
    else:
        p = line.rstrip('\n').split(" ")
        participants.append((int(p[0]), "d"))
        participants.append((int(p[1]), "f"))

# liste ordonnee par date evenement
participants = sorted(participants)

inter_max = 0
inter = 0

for participant in participants:
    if participant[1] == "d":
        inter += 1
    else:
        if inter_max < inter:
            inter_max = inter
        inter -= 1

print(inter_max)