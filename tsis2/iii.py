grocery_list = ["apple", "milk", "bread", "tea"]
for i in grocery_list:
    if i == "bread":
        continue
    print(i)

for i in grocery_list[0]:
    print(i)

for i in range(1, 16, 4):
    print(i)
else:
    print("Finished!")


adj = ["good", "bad"]
things = ["dress", "table"]

for i in adj:
  for j in things:
    print(i, j)