#-*-coding:utf8;-*-
#qpy:3
#qpy:console
'''
How tf are you supposed to do this under a minute
'''
import time
def streak(number):
    divisor = 1
    while number % divisor == 0: #20.38s for 11 i's P(i,4 ** i)
        divisor += 1
        number += 1
    return divisor - 1

#Define P(s,N) to be the number of integers n, 1<n<N, for which streak(n)=s.
def P(s,N):
    count = 0
    for number in range(2,N):
        if streak(number) == s:
            count += 1
    return count

s = time.time()
'''
streaks = {number:streak(number)
           for number in range(2,4 ** 11)
           }

Sum = 0
for i in range(1,12):
    for number in range(2,4 ** i):
        if streaks[number] == i:
            Sum += streaks[number] # 21s
'''
Sum = 0
for i in range(1,32):
    Sum += P(i,4 ** i) #19s

print(Sum)
print(time.time() - s)