list1 = ["apple", "orange", "banana", "pineapple", "mango"]
list2 = ["a", 36, False, 27, "apple"]
list3 = ["agjs", 4, 6]
list4 = [4, 28, 29, 10, 9]

list3.pop(1)
list1[1:3] = ["melon", "cherry"]
list2.insert(2, True)
list2.extend(list3)
list4.sort(reverse = True)

print(list4)
print(list1)
print(len(list2))

newlist = [x if x != "melon" else "orange" for x in list1]

print(newlist)

"""
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
"""