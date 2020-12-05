#!/usr/bin/python3
'''
@author edoardottt
'''
starting_year = 2010
current_year = 2020

def pad_number(inp, length):
    if len(str(inp))==length: return str(inp)
    return (length - len(str(inp))) * "0" + str(inp)

with open("YYYYMMDD-list.txt","w+") as f:
    for y in range(starting_year,current_year + 1):
        for m in range(1, 13):
            for d in range(1,32):
                f.write(pad_number(y,4) + pad_number(m,2) + pad_number(d,2) + "\n")

