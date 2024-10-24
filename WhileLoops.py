### Part Two -- your code goes here. 
import random

correct_number = random.randint(1, 100)

guessed_correctly = False

while not guessed_correctly:
    user_guess = int(input("Guess A Number"))

    if user_guess < correct_number:
        print("Higher")
    elif user_guess < correct_number:
        print("Lower!")
    else:
        guessed_correctly = True
        print("Well Done! You Got It!")
