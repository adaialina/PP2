x = 546
y = 742

if y > x:
  print("y is greater than x")
else:
  print("y is not greater than x")
print(isinstance(x, int)) # isinstance() determines datatype

# will return false
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))