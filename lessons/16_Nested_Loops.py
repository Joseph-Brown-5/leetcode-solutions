# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

for x in range(3):
    for y in range(1, 10):
        print(y, end=" ")  # you can set the print line end to whatever you want
    print()
