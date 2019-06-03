#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import time
def is_triangle(number):
    x = 1
    while number > 0:
        number -= x
        x += 1
    return number == 0

def factorizer(number,limit):
    a = []
    Range = number
    gate = isinstance(limit,int)
    
    x = 1
    while x < Range:
        """
        if x % round(number / 100) == 0:
            print("Iteration: {}".format(x))
            """
        if number % x == 0:
            a.append(x)
            a.append(int(number / x))
            Range = int(number / x)
            if gate:
                if len(a) > limit:
                    break
        x += 1
    
    a.sort()
    return a
    
def tri_gen(cap,tri_list):
    tri_num = tri_list[-1]
    x = len(tri_list)
    """
    while tri_num < cap:
        tri_num += x
        x += 1
        tri_list.append(tri_num)
        """
    tri_num = int(0.5 * x * (x + 1))
    tri_list.append(tri_num)
    return tri_list
s = time.time()
tri_list = [0]

while True:
    tri_list = tri_gen(tri_list[-1] + tri_list.index(tri_list[-1]) + 1,tri_list)
    if len(factorizer(tri_list[-1],"")) > 500:
        result_factors = factorizer(tri_list[-1],"")
        print("Success! Result: {}\nHas {} divisors: {}\n{} s".format(tri_list[-1],len(result_factors),result_factors,time.time() - s))
        break