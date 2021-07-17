from operator import itemgetter
import sys

current_year = 0
max_temp = 0
temp = 0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    year, temp = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        year = int(year)
        temp = int(temp)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_year == year:
        max_temp = max(max_temp, temp)
    else:
        if current_year != 0:
            # write result to STDOUT
            print('%d\t%d' % (current_year, max_temp))
        max_temp = temp
        current_year = year

# do not forget to output the last word if needed!
if current_year == year:
    print('%d\t%d' % (current_year, max_temp))