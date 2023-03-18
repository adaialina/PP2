import re
str = input()
a = re.findall("a.*b$", str)
if a:
    print('yes')
else:
    print('no')