import re 
st = str(input())
aAndBs = re.search("ab*", st)

if aAndBs:
    print("Yes")
else:
    print("No")