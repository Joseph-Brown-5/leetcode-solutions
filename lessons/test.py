def zigzagger(s, numRows):
    # zig
    flipper = 0
    row = 0
    stepper = 0
    middleCount = 0
    zigVar = 1
    zagStep = 0
    container = [[] for _ in range(numRows)]
    
    for x, character in enumerate(s):
        if flipper == 0:
            if stepper <= numRows:
                container[row].append(character)
                stepper += 1
                row += 1
            if stepper == numRows:
                flipper = 1
                stepper = 0
                row = 0
        elif flipper == 1:
            while middleCount <= (numRows):
                if middleCount == (numRows - zigVar):
                    container[numRows - zigVar].append(character)
                    middleCount += 1
                    zigVar += 1
                else:
                    container[middleCount-1].append(" ")
                    middleCount += 1
                zagStep += 1
                if zagStep == (numRows - 2):
                    flipper = 0
                    zigVar = 1
                    zagStep = 0
                    middleCount = 0
        

    for row in container:
        print("".join(row))

    # zag

    return
    


s = "paypalishiring"

r = int(input("how many rows: "))

zigzagger(s,r)
