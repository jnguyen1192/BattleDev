# *******
# * Read input from STDIN
# * Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
# * Use: sys.stderr.write() to display debugging information to STDERR
# * ***/
import sys


def date_res(i):
    i_end = i + 59
    day = int(i / 1440) + 1

    hour = int((i % 1440) / 60)
    hour_end = int((i_end % 1440) / 60)
    if hour < 10:
        hour = "0" + str(hour)
    if hour_end < 10:
        hour_end = "0" + str(hour_end)
    minute = int((i % 1440) % 60)
    minute_end = int((i_end % 1440) % 60)
    if minute < 10:
        minute = "0" + str(minute)
    if minute_end < 10:
        minute_end = "0" + str(minute_end)
    return str(day) + " " + str(hour) + ":" + str(minute) + "-" + str(hour_end) + ":" + str(minute_end)


lines = []
for line in sys.stdin:
    # sys.stderr.write(line.rstrip('\n') + '\n')
    lines.append(line.rstrip('\n'))
sys.stderr.write('beg\n')
dates = sorted(lines[1:])
limi_beg = "08:00"
limi_end = "17:59"

schedule = []
for date in dates:
    day = (int(date[0]) - 1) * 1440
    beg = int(date[2:4]) * 60 + int(date[5:7]) + day
    end = int(date[8:10]) * 60 + int(date[11:13]) + day
    schedule.append((beg, end))
    sys.stderr.write(date + "\n")
    sys.stderr.write(str(beg) + " " + str(end) + "\n")
# brute force
end = False
for j in range(0, 7):
    test = False
    if end:
        break
    for i in range(8 * 60 + 1440 * j, 8 * 60 + 10 * 60 + 1440 * j):
        if end:
            break
        for dates in schedule:
            if (i > dates[0] and i <= dates[1]) or (i + 59 >= dates[0] and i + 59 < dates[1]):
                test = True
                break
        if not test:
            sys.stderr.write("i finale : " + str(i) + "\n")
            print(date_res(i))
            end = True



