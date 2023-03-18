import re
str = input()
a = re.sub("[\s,.]", ":", str)

print(a)