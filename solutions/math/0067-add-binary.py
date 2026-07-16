<<<<<<< HEAD
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
=======
# 1st solution: time complexity: O(N), beats: 52.88%
# this took way longer than i want to admit lol. ended up looping through based on the length of the strings and
# abused if statments for each case using a carry variable to handle the binary addition logic.

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        if len(a) > len(b):
            while len(a) > len(b):
                b = "0" + b
        elif len(b) > len(a):
            while len(b) > len(a):
                a = "0" + a

        carry = "0"
        solution = ""
        place = len(a) - 1

        for thing in a:
            if a[place] == "1" and b[place] == "1" and carry == "0":
                solution += "0"
                carry = "1"
            elif a[place] != b[place] and carry == "1":
                solution += "0"
            elif a[place] != b[place] and carry == "0":
                solution += "1"
            elif a[place] == "0" and b[place] == "0" and carry == "1":
                solution += "1"
                carry = "0"
            elif a[place] == "0" and b[place] == "0":
                solution += "0"
            elif a[place] == "1" and b[place] == "1" and carry == "1":
                solution += "1"
            place -= 1

        if carry == "1":
            solution += carry

        solution = solution[::-1]
        return solution

# a better solution which (imo) is not in the spirit of the question but it works

        return bin(int(a, 2) + int(b, 2))[2:]
<<<<<<< HEAD

    # update for git
=======
>>>>>>> 35d673538edc858b4769c332522acbb90beded70
>>>>>>> 51dd203827b186c4e4935c22dce4c0ccf3e8117d
