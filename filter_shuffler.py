import numpy, random, sys

from datetime import datetime


def mixItUp(filter_filename):
    items = []

    with open( filter_filename ) as file:
        for line in file: items.append(line)

        file.close()

        random.shuffle(items)

    time_str = ((str(datetime.now()).replace(' ','-')).replace(':','_'))[:19]


    with open( time_str+"_filter.txt", "w" ) as outFile:
        outFile.writelines(items)

mixItUp(sys.argv[1])
