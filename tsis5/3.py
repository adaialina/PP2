import re
str = input()
a = re.findall("[^A-Z]\w+_\w+", str)
if a:
    print('found')
else:
    print('not found')