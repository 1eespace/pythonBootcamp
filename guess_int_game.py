# Task 2: Create a game where the user must correctly guess a randomly generated integer between 1 and 100
# The user should be notices whether their guess was "lower" or "higher" than the target number

# Step1. use "random" library's randint function 
import random

# Use function to group code
# Try to have functions that only do one thing (oop: SRP)
# print a message, validate user input, check what message to display
# Check for invalid inputs, notifying the user and re-prompting for a valid input

def guessing_game():
    correct_answer = random.randint(1, 100)

    while True:
        user_prompt = int(input("Enter the number: "))

        if user_prompt < correct_answer:
            print('higher')
        
        elif user_prompt > correct_answer:
            print('lower')

        else:
            print('right')
            break

guessing_game()


