# *******
# * Read input from STDIN
# * Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
# * Use: sys.stderr.write() to display debugging information to STDERR
# * ***/
import sys
import time

start_time = time.time()

# Trie la liste pour le debut et la fin en gardant un index commun

# sys.stderr.write("Before read lines \n")
# lines = []
participants = []
nb_participant = 0
# sys.stderr.write("Before create participants \n")

for line in sys.stdin:
    if nb_participant == 0:
        nb_participant = line
    else:
        p = line.rstrip('\n').split(" ")
        participants.append((int(p[0]), int(p[1])))

# participants = [(int(line.split(" ")[0]), int(line.split(" ")[1])) for line in lines[1:]]

# sys.stderr.write("Before sort " + str(len(participants)) + "\n")
# liste ordonnee par debut
participants = sorted(participants)

participants_en_cours = []
sys.stderr.write("After sort " + str(len(participants)) + "\n")

inter_max = 0
for participant in participants:
    added = False
    # ajout du participant dans la liste des participants en cours
    for i, p in enumerate(participants_en_cours):
        # au bon endroit
        if participant[1] < p[1]:
            participants_en_cours.insert(i, participant)
            added = True
            break

    if not added:
        participants_en_cours.append(participant)

    # participants_en_cours.append(participant)
    # mettre a jour la liste des participants en cours en fonction du nouveau participant en cours
    # participants_en_cours = sorted(participants_en_cours, key=lambda part: part[1])
    for p in participants_en_cours:
        if p[1] < participant[0]:
            # sys.stderr.write("remove " + str(participant[0]) +" " + str(participant[1]) + "\n")
            participants_en_cours.remove(p)
        else:
            break
            # mettre a jour la variable inter
    inter = len(participants_en_cours)
    if inter > inter_max:
        inter_max = inter
    # sys.stderr.write(str(participant[0]) +" " + str(participant[1]) + "\n")
# sys.stderr.write(str(inter_max)+ "\n")

end_time = time.time()
sys.stderr.write(str(end_time - start_time) + "\n")
print(inter_max)