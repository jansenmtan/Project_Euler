#-*-coding:utf8;-*-
#qpy:3q

#qpy:console
import time

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
    cap = 1000
    num_sols = {x : 0 for x in range(1,cap)}
    dupes = set()
    for a in range(1,cap // 2):
        for b in range(a,(cap - a) // 2):
            if a % 2 != 0 and b % 2 != 0:
                continue
            
            c = (a**2 + b**2)**0.5
            
            if all([a + b + c < cap,c % 1 == 0,(a,b) not in dupes,(b,a) not in dupes]):
                #print("{}^2 + {}^2 = {}^2".format(a,b,int(c)))
                num_sols[a + b + c] += 1
                
    Max = max(num_sols,key = num_sols.get)
    print("{}: {}".format(Max,num_sols[Max]))
    """
    count = 0
    for i in range(1,cap):
        count += num_sols[i]
    print(count)
    """

main()