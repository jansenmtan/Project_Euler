#-*-coding:utf8;-*-
#qpy:3
#qpy:console

distinct_terms = {a**b
                  for a in range(2,101)
                  for b in range(2,101)}

print(len(distinct_terms))
