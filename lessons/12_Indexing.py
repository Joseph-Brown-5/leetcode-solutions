# indexint = accessing elemts of a sequence using [] (indexing operator)
#           [start : end : step]

credit_number = "1234-5678-9012-3456"

print(f"Credit Card Number: {credit_number}")
print(f"0 {credit_number[0]}")
print(f":4 {credit_number[:4]}")
print(f"5:9 {credit_number[5:9]}")
print(f"5: {credit_number[5:]}")
print(f"-1 {credit_number[-1]}")
print(f"::3 {credit_number[::3]}")