# python compound interest calculator

# A = P(1+r/n)^t
# A = final amount
# P = initial principal balance
# r = interest rate
# t = number of time periods elapsed


# take user input for intial, the interest rate, and the number of time periods
principle = 0
interest_rate = 0
elapsed_periods = 0

while principle <= 0:
    principle = float(input("Please provide the principle balance: "))
    if principle <= 0:
        print("Principle cannot be less than or equal to 0")

while interest_rate <= 0:
    interest_rate = float(input("Please provide the interst rate: "))
    if interest_rate <= 0:
        print("principle cannot be less than or equal to 0")

while elapsed_periods <= 0:
    elapsed_periods = int(input("Please provide the elapsed time periods: "))
    if elapsed_periods != int:
        print("Time periods must be integers.")
    elif elapsed_periods <= 0:
        print("Time periods must be greater than 0.")

# do the math
Total = principle * pow((1 + (interest_rate / 100)), elapsed_periods)

# print it out
print(f"The total is: ${Total:.2f} after {elapsed_periods} years!")
