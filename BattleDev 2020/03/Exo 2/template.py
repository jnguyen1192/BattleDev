#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
numbers = lines[1:]

acc = 1
res = 0
previous = numbers[0]
sys.stderr.write("Begin\n")
for number in numbers[1:]:
    sys.stderr.write(number + "\n")
    if number == previous:
        acc += 1
        if acc > res:
            res = acc
    else:
        acc = 1
    previous = number
print(res)