#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import time
from itertools import count

#decorator that gets time of program
def dect(func):
    def timef():
        t0 = time.time()
        func()
        t1 = time.time()
        print(t1 - t0)
    return timef

def is_pandigital(num_list):
    ds = "".join([str(num) for num in num_list])
    if len(ds) != 9:
        return False
    elif ("0" in ds or
        max({ds.count(d) for d in ("1","2","3","4","5","6","7","8","9")}) > 1):
        return False
    else:
        return True

@dect
def main():
    largest = 0
    for num in range(1,100000):
        concan = ""
        for Int in count(1):
            if len(concan) < 9:
                concan += str(num * Int)
            else:
                if all([is_pandigital([concan]),Int > 2,int(concan) > largest]):
                    largest = int(concan)
                break
    print(largest)
main()