import re
st = input()
a = re.findall("[A-Z]+[a-z]+$", st)
if a:
    print('found')
else:
    print('not found')