#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import os

os.chdir("/storage/emulated/0/qpython/scripts3/Project_Euler")
with open("p022_names.txt") as names:
    names = list(names)[0].split(",")
    names.sort()

    alph_ord = {"A":1,
                "B":2,
                "C":3,
                "D":4,
                "E":5,
                "F":6,
                "G":7,
                "H":8,
                "I":9,
                "J":10,
                "K":11,
                "L":12,
                "M":13,
                "N":14,
                "O":15,
                "P":16,
                "Q":17,
                "R":18,
                "S":19,
                "T":20,
                "U":21,
                "V":22,
                "W":23,
                "X":24,
                "Y":25,
                "Z":26,
                "\"":0,
                "\'":0,
                }

    name_value = {name:sum([alph_ord[char] for char in name]) * (names.index(name) + 1)
                  for name in names}

    '''
    for name in names:
        addends = [alph_ord[char]
                   for char in name]
        name_value[name] = sum(addends) * (names.index(name) + 1)
    '''

print(sum(name_value.values()))