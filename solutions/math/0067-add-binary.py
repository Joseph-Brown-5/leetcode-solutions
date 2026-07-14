a = "11"
b = "1"
solution = ""
carry = "0"

if len(a) > len(b):
    while len(a) > len(b):
        b += "0"
        print(f"b: {b}")
elif len(b) > len(a):
    while len(b) > len(a):
        a += "0"
        print(f"a: {a}")

print(b[::-1])
if a[::-1] and b[::-1] == 1:
    solution += "0"
    carry = "1"
    print(f"solution: {solution}")
elif (a[::-1] != b[::-1]) and carry == "1":
    solution += "0"
    print(f"solution: {solution}")
else:
    solution += "1" 
    print(f"solution: {solution}")

if carry == "1":
    solution += "1"

solution = solution[::-1]
print(solution)