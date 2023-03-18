import re 
def camel(string):
    c = re.findall("[A-Z][^A-Z]*", string)
    answers = " ".join(c)
    return answers

a = input()
b = re.sub("\s", "_", camel(a).lower())

print(b)