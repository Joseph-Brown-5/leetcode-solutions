# logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be True
#                     and = both conditions must be True
#                     not = inverts the condition (not False, not True)


temp = int(input("What is the Temperature?: "))
# is_raining = False
is_sunny = True

# if temp > 35 or temp < 0 or is_raining:
#         print ("The outdoor event is cancelled")
# else:
#         print("The outdoor event is still scheduled")

if temp >= 28 and is_sunny:
    print("It is hot outside")
    print("It is sunny")
elif temp <= 0 and is_sunny:
    print("It is cold outside")
    print("It is sunny")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outside")
    print("It is sunny")
elif temp >= 28 and not is_sunny:
    print("It is hot outside")
    print("It is cloudy")
elif temp <= 0 and not is_sunny:
    print("It is cold outside")
    print("It is cloudy")
elif 28 > temp > 0 and not is_sunny:
    print("It is warm outside")
    print("It is cloudy")