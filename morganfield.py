#!/usr/bin/python

# Python 3 script based on the functionality of Cloakify - https://github.com/TryCatchHCF/Cloakify
# Encodes to base64, then rot13's all letters, then performs substitution based on a supplied filter.


# Filter files must have at least 66 entries


import random, sys, os, base64


def muddy(unencoded_item_filename, filter_filename, output_filename):


    b64_chars = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/+=")
    filter_info = []

    item_file = open( unencoded_item_filename , 'rb' )
    item_raw = item_file.read()
    item_b64 = str(base64.encodestring( item_raw ))[2:-3]


    with open( filter_filename ) as file:
        for line in file: filter_info.append(line)


    with open(output_filename, "w+") as outFile:
        for char in item_b64:
            if char != '\n':
                outFile.writelines( filter_info[ b64_chars.index(char) ] )



def clean(encoded_item_filename, filter_filename, output_filename):

    b64_chars = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/+=")
    undecoded = []
    filter_info = []
    dec_item_64=""

    with open( encoded_item_filename) as file:
        for line in file:
            undecoded.append(line.split('\n')[0])

    with open( filter_filename ) as file:
        for line in file:
            filter_info.append(line.split('\n')[0])


    for word in undecoded:
        dec_item_64 += b64_chars[ filter_info.index(word) ]


    #print (dec_item_64)
    with open(output_filename, "w+") as outFile:
        outFile.write(str(base64.b64decode( dec_item_64 ))[2:-1].replace('\\n','\n'))

        #outFile.write(str(base64.b64decode( dec_item_64 )))




if ( len(sys.argv) != 5 ):
    print ("Syntax: \"morganfield.py <item_filename> <filter_filename> <muddy/clean> <output_filename>\"")
    sys.exit()


if (sys.argv[3] == "muddy"):
    muddy(sys.argv[1], sys.argv[2], sys.argv[4])

elif (sys.argv[3] == "clean"):
    clean(sys.argv[1], sys.argv[2], sys.argv[4])

else:
    print ("Syntax: \"morganfield.py <item_filename> <filter_filename> <muddy/clean> <output_filename>\"")
    sys.exit()
