# if = Do some code only IF some condition is True
#       Else do something else

age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You havn't been born yet!")
else:
    print("You are to young!")
