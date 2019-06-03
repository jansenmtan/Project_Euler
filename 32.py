#-*-coding:utf8;-*-
#qpy:3
#qpy:console
from itertools import permutations

def factorizer(number,limit):
    a = []
    gate = isinstance(limit,int)
    
    for x in range(1,int(number**0.5 + 1)):
        if number % x == 0:
            a.append(x)
            a.append(int(number / x))
            Range = int(number / x)
            if gate == True:
                if len(a) > limit:
                    break
    
    a.sort()
    return a

def is_pandigital(num_list):
    ds = "".join([str(num) for num in num_list])
    if len(ds) != 9:
        return False
    elif ("0" in ds or
        max({ds.count(d) for d in ("1","2","3","4","5","6","7","8","9")}) > 1):
        return False
    else:
        return True

Sum = 0
#go through 3 factors; >3 factors is always false
#(checked with earlier versions)

#perhaps use strings? convert int to string,
#and add 1 (ie 678 -> 679 -> 689 -> 789)
s_num = "123"
while True:
    f_list = factorizer(int(f_sum),"")
    """
    for n1d2 in range(n1d1 + 1,10):
        n1 = n1d1 * 10 + n1d2
        prod = 2 * 3 * 4 * n1
        if is_pandigital([2,3,4,n1,prod]):
            Sum += prod
"""
print(Sum)