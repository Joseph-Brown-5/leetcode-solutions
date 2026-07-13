# dictionary = a collectino of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))

# prints the appropriate key value for the given variable
# print(capitals.get("India"))

# if a value is not present it will print none
# print(capitals.get("Japan"))

# check to see if a capital is in the dictionary
# if capitals.get(input("Provide a Country: ")):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

# this will add a value to the dictionary
# capitals.update({"Germany": "Berlin"})

# # this will update a value in the dictionary
# capitals.update({"USA": "D.C."})

# # this will remove a value in th edictionary
# capitals.pop("China")

# # this will remove the latest value added to the dictionary
# capitals.popitem()

# # this will clear the dictionary
# capitals.clear()

# print(capitals)

# this will only print the keys in the dictionary
# keys = capitals.keys()

# this will only print the values in the dictionary
# values = capitals.values()

# for value in capitals.values():
#     print(value)

# print("----------------------")

# for key in capitals.keys():
#     print(key)

# .items() returns a 2D list of touples. eg: [(),(),()]
items = capitals.items()

# GOOD WAY TO MOVE THOUGH 2D DATA UNILATERALLY
for key, value in capitals.items():
    print(f"{key}: {value}")
