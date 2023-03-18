a = 32
b = 56
c = 18
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

print("a") if a > b else print("=") if a == b else print("b")

if a > b or a > c:
  print("At least one of the conditions is true")

if b > a:
  pass