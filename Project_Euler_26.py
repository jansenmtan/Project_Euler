#-*-coding:utf8;-*-
#qpy:3
#qpy:console
"""
I remember back in 8th grade, bored in math class, I would see that certain numbers had
longer reciprocal cycles than others. I wanted to graph the function of 1/ a number
to its reciprocal number in base 10. I had no idea how in the fuck to even approach
doing that. I can do that now. 4 years later. Thanks Project Euler.
"""
from math import log
from math import log10
#does long division and
#returns the reciprocal cycle
def cycle_of(dividend):
    pairs = []
    remainder = 1
    partial_quo = remainder // dividend
    count = 0
    #for some reason count is zero-based??? wtf???
    while count < 1:
        count = pairs.count((partial_quo,remainder))
        pairs.append((partial_quo,remainder))
        remainder *= 10
        partial_quo = remainder // dividend
        remainder %= dividend
    #join the digits of the quotient
    str_cycle = "".join([str(pairs[i][0]) for i in range(1,len(pairs) - 1)])
    return str_cycle

max_recip_len = (0,"")
for number in range(1,1000):
    if any([log(number,2) % 1 == 0,
            log(number,5) % 1 == 0,
            log10(number) % 1 == 0,
            ]):
        continue
    cycle_of_num = (number,cycle_of(number))
    
    if len(cycle_of_num[1]) == max(len(cycle_of_num[1]),len(max_recip_len[1])):
        max_recip_len = cycle_of_num

print(max_recip_len)