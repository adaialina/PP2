tuple1 = ("Alisher", "Olzhas", "Aidana", "Dilya")
print(tuple1[-1]) #refers to the last item
print(tuple1[2:4])
print(tuple1[3:])

(Olzhas, Dilya, *As) = tuple1

print(As)

tuple2= ("Alina",) #with comma, otherwise it is str
x = ("Amina",)
tuple2 += x

#print(tuple2)

i = 0
while i < len(tuple2):
  print(tuple2[i])
  i = i + 1

new_tuple = tuple2 * 2
print(new_tuple)