import re
a = input()
b = re.findall("[A-Z][a-z]*", a)

c = " ".join(b)
print(c)