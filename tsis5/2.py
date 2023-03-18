import re
str = input()
if re.search('ab{2,3}', str):
    print("Yes")
else:
    print("No")