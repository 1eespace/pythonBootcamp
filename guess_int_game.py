# Task 2: Create a game where the user must correctly guess a randomly generated integer between 1 and 100
# The user should be notices whether their guess was "lower" or "higher" than the target number

# Step 1. use "random" library's randint function 
import random

# Use function to group code
# Try to have functions that only do one thing (oop: SRP)
# print a message, validate user input, check what message to display
# Check for invalid inputs, notifying the user and re-prompting for a valid input

# Step 2. make 3 situations message
def correct_message():
    print("You got it!")

def higher_message():
    print("higher")

def lower_message():
    print("lower")

# Step 3. check user's input validation (input/answer)
def check_input_validate(user_input, correct_answer):
    # If user_input is smaller then correct_answer,
    # user must to type higher num than the previous
    if user_input < correct_answer:
        higher_message()

    # If user_input is bigger then correct_answer,
    # user must to type lower num than the previous
    elif user_input > correct_answer:
        lower_message()

    # If user_input == correct_number, shows/print the success message
    else:
        correct_message()

# Step 4. Combine all together
def guessing_game():
    # Use random library with randint for choosing the number randomly (1 to 100)
    correct_answer = random.randint(1, 100)

    # Use "while" loop; For showing enter prompt until the game finished
    while True:
        user_input = int(input("Enter a number between 1 and 100: "))
        # Use Step 3 function for comparing the user's input with the answer
        check_input_validate(user_input, correct_answer)

        if user_input == correct_answer:
            # If user_input == correct_number, stop the game
            break

# Step 5. Call the function
guessing_game()
