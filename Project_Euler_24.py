#-*-coding:utf8;-*-
#qpy:3
#qpy:console
"""
I'd like to make the permutation code myself,
but that's too much for me
"""
from itertools import permutations

print(list(permutations([0,1,2,3,4,5,6,7,8,9]))[10**6 - 1])