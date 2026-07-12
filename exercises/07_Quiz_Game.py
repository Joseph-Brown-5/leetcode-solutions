# Python quiz game

questions = (("How many elements are in the periodic table?: "),
             ("Which animal lays the largest eggs?: "),
             ("What is the most abundant gas in Earth's atmosphere?: "),
             ("How many bones are in the human body?: "),
             ("Which planet in the solar system is the hottest?: "))

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")

guesses = []
score = 0
question_num = 0

print("------------ QUIZ TIME ------------")

# print a question in a loop that moves one question to the next
n = 0
a = 0

for question in questions:
    print(question)

    for option in options[n]:
        print(option)

    answer = input("Please choose your answer: ")
    if answer == answers[a]:
        score += 20

    a += 1
    n += 1
print(f"Your Score: {score}/100")

# take the user input as A B C or D
# check the guess and if correct add to score
# print out total score at the end
