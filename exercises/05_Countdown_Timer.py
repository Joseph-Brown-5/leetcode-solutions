import time

# # the time.sleep(seconds) function takes input and delays the given amount of time before continuing
# time.sleep(3)

# print("TIME'S UP!")

# what I want:
# take user input for how long the timer needs to run


# what I made

# given_time = int(input("Set Timer (seconds): "))
# increment = int(input("Set Countdown Increment (Seconds): "))
# remaining_time = given_time

# while remaining_time > 0:
#     time.sleep(increment)
#     remaining_time -= increment
#     print(remaining_time)

# print("DONE!")


# from the course
# deffinetely a better implementation and a more useful timer (I need to start pushing myself to make more
# finished products)

my_time = int(input("Enter the time in seconds: "))

# using the built in range function is better than while probably
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")
