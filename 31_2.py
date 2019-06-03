#-*-coding:utf8;-*-
#qpy:3
#qpy:console

#break apart 200 into 100s, 100s into 50s, etc
#1,2,5,10,20,50,100,200

uniques = set()
s = [200] #s for start
uniques.add(str(num) for num in s)
while max(s) > 1:
     f = -1
     while s[f] == 1:
          f -= 1
     
     h = s.pop(f)
     
     if h == 200:
          s.extend((100,100))
     elif h == 100:
          s.extend((50,50))
     elif h == 50:
          s.extend((20,20,10))
     elif h == 20:
          s.extend((10,10))
     elif h == 10:
          s.extend((5,5))
     elif h == 5:
          s.extend((2,2,1))
     elif h == 2:
          s.extend((1,1))
     
     uniques.add(".".join(str(num) for num in s))

s = [200]
while max(s) > 1:
     h = s.pop(s.index(max(s)))
     
     if h == 200:
          s.extend((100,100))
     elif h == 100:
          s.extend((50,50))
     elif h == 50:
          s.extend((20,20,10))
     elif h == 20:
          s.extend((10,10))
     elif h == 10:
          s.extend((5,5))
     elif h == 5:
          s.extend((2,2,1))
     elif h == 2:
          s.extend((1,1))
     
     uniques.add(".".join(str(num) for num in s))

print(len(uniques))
