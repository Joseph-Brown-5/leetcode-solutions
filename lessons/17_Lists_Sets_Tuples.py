# collection = single "variable" used to store multiple values
#   Lists = [] ordered changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. No duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# normal variable
fruit = "apple"

print(fruit)

# ------------------------ lists ------------------------ #

fruits = ["apple", "orange", "banana", "coconut"]
# print(dir(fruits))      # prints the methods you can use with the given variable
# print(help(fruits))     # shows it in greater detail

print(fruits)
print(fruits[2])
print(fruits[::2])
print(fruits[-1])
# print(fruits[4]) this will throw an indexing error

# most people would rename x to fruit (or a singular variable)
for x in fruits:
    print(x)

# prints the length of the list
print(len(fruits))

# checks if a value is present in a list
print("apple" in fruits)
print("pineapple" in fruits)

# fruits[0] = "pineapple"         # replaces the given variable with the new variable
# fruits.append("pineapple")      # adds the given value to the end of the list
# fruits.remove("apple")          # removes the given value from the list
# fruits.insert(0, "pineapple")   # inserts the given value at the given index
# fruits. sort()                  # will sort strings in alphabetical order or in ascending numerical order
# fruits.reverse()                # will reverse the list (will not "sort the list will print it in reverse order as is")
# fruits.clear()                  # will empty out a list
# fruits.index("apple")           # will give the index of the given variable (will throw an error if not present)
# fruits.count("banana")          # will print the amount of times the given variable is present

for x in fruits:
    print(x)

fruits.append("pineapple")

# ------------------------ Sets ------------------------ #

fruits = {"aaple", "orange", "banana", "coconut"}

# print(dir(fruits))
# print(help(fruits))

# print(fruits[0])               # will throw an error because sets are unordered and cannot be indexed
# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()                    # this will remove the "first" object but because sets are unordered it will be random

# ------------------------ Tuples ------------------------ #

fruits = ("apple", "orange", "banana", "coconut", "coconut")

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

print(fruits.index("apple"))
print(fruits.count("coconut"))
