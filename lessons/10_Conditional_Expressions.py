# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          x if condition else y


num = 5
a = 6
b = 7
age = 13
temperature = 30
user_role = "guest"

print("Positive" if num > 0 else "Negative")
result = "Even" if num % 2 == 0 else "ODD"
max_num = a if a > b else b
min_num = a if a < b else b
status = "adult" if age >= 18 else "Child"
weather = "Hot" if temperature > 20 else "Cold"
access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(result)
print(max_num)
print(status)
print(weather)
print(access_level)
