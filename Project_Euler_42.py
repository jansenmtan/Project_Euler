#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import time
import os

#decorator that gets time of program
def dect(func):
    def timef():
        t0 = time.time()
        func()
        t1 = time.time()
        print(t1 - t0)
    return timef

def is_triangular(number):
    x = 1
    while number > 0:
        number -= x
        x += 1
    return number == 0

@dect
def main():
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

    path = "/sdcard/qpython/scripts3/Project_Euler/"
    os.chdir(path)
    
    with open(path + "p042_words.txt","r") as F:
       words = list(F)[0].split(",")
    words.sort()
    
    count = 0
    for word in words:
        Sum = 0
        for char in word:
            
            Sum += alph_ord[char]
            """
            if char == '"':
                continue
            Sum += ord(char) - 64
            """
        if is_triangular(Sum):
            count += 1
    print(count)

main()