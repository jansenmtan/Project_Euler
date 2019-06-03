#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import time
s = time.time()
"""
I initially brute-forced it all the way, and it was a little slow, but after glancing in this forum, I made it only try odd numbers ≥500001
- strupo, Wed 2 Aug 2017

Maybe I should do that!
"""
min = 500001
cap = 10**6
cycle = []
cycle_lengths = {}

for num in range(min,cap,2):
    onum = num
    """
    if num % 1 == 0:
        print("Testing {}...".format(num))
    """
    cycle.append(num)
    
    while True:
        if num % 2 == 0:
            num /= 2
        else:
            num = 3 * num + 1
        
        if cycle[-1] == 1:
            break
            
        cycle.append(num)
    
    cycle_lengths.update({int(onum):int(len(cycle))})
    
    del cycle[:]

string = "{} has the longest Collatz cycle. It is {} steps long.\n {} s"

print(string.format(max(cycle_lengths,key = cycle_lengths.get),
                    max(cycle_lengths.values()),
                    time.time() - s,
                    ))