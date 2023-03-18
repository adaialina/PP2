set1 = {"orange", True, 4, 97, "black"}
set2 = {1, 2, 3, 4, 5}
set3 = {True, False}

set1.add("white")
set2.update(set3)
set2.discard(True)

print(set1)
print("orange" in set1)
for x in set2:
  print(x)


a = {"apple", "banana", "orage"}
b = {"red", "orange", "blue"}

c = a.symmetric_difference(b) #intersection is the oppposite

print(c)

#union and update exclude duplicates
#del deletes the set completely
#clear() empties the set