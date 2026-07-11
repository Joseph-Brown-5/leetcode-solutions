# for loops = execute a block of code a fixed number of times
#             you can iterate over a range, string, sequence, etc.
#             range(start, stop, step)

for x in range(1, 11):    # counts 1 -> 10
    print(x)
print("--------------------------")

for x in reversed(range(1, 11)):    # counts 10 -> 1
    print(x)
print("--------------------------")

for x in range(1, 11, 2):   # counts 1 -> 10 (by 2's)
    print(x)
print("--------------------------")

credit_card = "1234-5678-9012-3456"

for x in credit_card:  # iterates thought the given string one step at a time
    print(x)
print("--------------------------")

for x in range(1, 21):  # iterates through the list but "skips" 13, if break is enabled it stops at 13 instead
    if x == 13:
        continue
       # break
    else:
        print(x)
print("--------------------------")
