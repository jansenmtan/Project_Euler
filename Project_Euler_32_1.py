#-*-coding:utf8;-*-
#qpy:3
#qpy:console
#fuck groups. shit gets out of hand and is hard to think about
#also FUCK ME this shit takes 30 fucking seconds when some can do it in a second
import time
from itertools import permutations

#decorator that gets time of program
def dect(func):
    def timef():
        t0 = time.time()
        func()
        t1 = time.time()
        print(t1 - t0)
    return timef

@dect
def main():
    perms = list(permutations([str(x) for x in range(1,10)]))
    valid = []
    for Tuple in perms:
        for f1_l in range(1,5):
            f1 = int("".join(Tuple[:f1_l]))
            
            for f2_l in range(1,5):
                if f1_l + f2_l > 6:
                    break
                
                f2 = int("".join(Tuple[f1_l:f1_l + f2_l]))
                prod = int("".join(Tuple[f1_l + f2_l:]))
                
                if f1 * f2 == prod:
                    valid.append((f1,f2,prod))
    
    dupes = set()
    for prod in list(valid):
        if prod[2] in dupes:
            del valid[valid.index(prod)]
        else:
            dupes.add(prod[2])
    
    for eqtn in valid:
        print("{} * {} = {}".format(eqtn[0],eqtn[1],eqtn[2]))
    print("Final sum: {}".format(sum([eqtn[2] for eqtn in valid])))

main()
