import re
a = input()
b = re.sub("[_]"," ", a)
c = re.split("\s", b)
for i in range(1, len(c)):
    print(c[0]+""+c[i].capitalize(), end='')