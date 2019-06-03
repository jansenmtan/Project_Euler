#-*-coding:utf8;-*-
#qpy:3
#qpy:console
#slow brute force method; trying to comment better
import time
from itertools import permutations

#decorator that gets execution time of program
def dect(func):
    def timef():
        t0 = time.time()
        func()
        t1 = time.time()
        print(t1 - t0)
    return timef

@dect
def main():
    #as for everything pandigital, a list of permutations will be used
    nums = list(permutations([str(x) for x in range(10)]))
    prime = (2,3,5,7,11,13,17)
    
    Sum = 0
    #for every permutation,
    for num in nums:
        #a flag will be used to mark bad numbers
        flag = 0
        Num = int("".join(num))
        
        #get three digits from num starting from 2nd digit
        for i in range(1,8):
            numb = int("".join(num[i : (i + 2) + 1]))
            
            #check if those three digits are a multiple of the i-th prime
            if numb % prime[i - 1] != 0:
                #if not, dont bother checking the other digits
                flag = 1
                break
        
        if flag == 0:
            print("{}: {}".format(Num,nums.index(num)))
            Sum += int(Num)
    print(Sum)

main()