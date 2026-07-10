# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Please provide us with your username: ")

if len(username) > 12: 
    print("Username is to long")
elif username.isalpha() != True:
     print("Username cannot contain spaces or numbers")
else: 
    print(f"Congrats {username}")