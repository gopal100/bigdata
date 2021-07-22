#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # print(line)
    # split the line into words
    words = line.split(",")
    year = ''
    if len(words) == 3:
        if "-" in words[0]:
            year = words[0].split("-")[2]
        # print(year, words[2])
        print('%s\t%s' % (year, words[2]))
