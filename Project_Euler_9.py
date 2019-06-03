#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def is_Pythlet(a,b,c):
    return ((a < b and b < c) and
           (a**2 + b**2 == c**2))

for a in range(1,500):
    for b in range(a,500):
        c = int((a**2 + b**2)**0.5)
        if    (is_Pythlet(a,b,c) and
              (a + b + c == 1000)):
            print("{}, {}, {}\n{}".format(a,b,c,a * b * c))