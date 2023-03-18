dict1 = {
  "brand": "Dior",
  "luxury": True,
  "year": 1996,
  "colors": ["white", "black", "green"]
}

print(type(dict1))

x = dict1.keys()
print(x) #before the change

dict1["country"] = "France" # or dict1.update({"country": "France"})
print(x) #after the change

dict2 = dict(name = "Dina", age = 18, country = "KZ")

dict2.update({"country": "USA"})
del dict2["18"]

if "USA" in dict2:
    print("Yes, Dina is USA")

for x in dict2:
    print(x)      #keys

for x in dict2:
    print(dict2[x]) #values

for x, y in dict2.items():
  print(x, y)      #both

# nested dict
rooms = {
    "room1" : {
        "name" : "Symbat",
        "floor" : 4
    },
    "room2" : {
        "name" : "Amina",
        "floor" : 2
    },
    "room3" : {
        "name" : "Aru",
        "floor" : 7
    }
}

print(rooms)

# we can nest separate dicts into 1