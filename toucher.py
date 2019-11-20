# *******
# * Read input from STDIN
# * Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
# * Use: sys.stderr.write() to display debugging information to STDERR
# * ***/
import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

nb_touch_bog = lines[0]
touch_bogs = lines[1].split(" ")
touch_corrs = lines[2].split(" ")
chaine_a_traduire = lines[3]

chaine_traduite = ""
sys.stderr.write(" ".join(touch_bogs))
sys.stderr.write("\n")
sys.stderr.write(" ".join(touch_corrs))
sys.stderr.write("\n")
sys.stderr.write(chaine_a_traduire)
sys.stderr.write("\n")
for c in chaine_a_traduire:
    # sys.stderr.write("char " + c + "\n")
    for i, t in enumerate(touch_bogs):
        if c.lower() == t:
            # respect min/maj
            if c.isupper():
                chaine_traduite += touch_corrs[i].upper()
            else:
                chaine_traduite += touch_corrs[i]
    if c.lower() not in touch_bogs:
        chaine_traduite += c

sys.stderr.write(chaine_traduite + "\n")
print(chaine_traduite)

