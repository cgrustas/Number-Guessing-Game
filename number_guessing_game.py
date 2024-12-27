# Coleman Grustas
# 12/27/2024
# Number Guessing Game

import random

MIN = 1 # lowest integer in guessing game
MAX = 100 # highest integer in guessing game

EASY = 10 # number of guesses on easy mode
MEDIUM = 5 # number of guesses on medium mode
HARD = 3 # number of guesses on hard mode


# - When the game starts, it should display a welcome message along with the rules of the game.
# - The computer should randomly select a number between MIN and MAX.
# - User should select the difficulty level (easy, medium, hard) which will determine the number of chances they get to guess the number.
# - The user should be able to enter their guess.
# - If the user’s guess is correct, the game should display a congratulatory message along with the number of attempts it took to guess the number.
# - If the user’s guess is incorrect, the game should display a message indicating whether the number is greater or less than the user’s guess.
# - The game should end when the user guesses the correct number or runs out of chances.


def main():
    # - When the game starts, it should display a welcome message along with the rules of the game.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 5 chances to guess the correct number.")
    print()

    # - The computer should randomly select a number between 1 and 100.
    random_number = random.randint(MIN, MAX)
    
    # - User should select the difficulty level (easy, medium, hard) which will determine the number of chances they get to guess the number.
    print("Please select the difficulty level: ")
    print(f"1. Easy ({EASY} chances)")
    print(f"2. Medium ({MEDIUM} chances)")
    print(f"3. Hard ({HARD} chances)")
    print()
    
    difficulty_name = None
    chances = None
    while True:
        difficulty_level = int(input("Enter your choice: "))
        if difficulty_level == 1:
            difficulty_name = "Easy"
            chances = 10
            break
        elif difficulty_level == 2: 
            difficulty_name = "Medium"
            chances = 5
            break
        elif difficulty_level == 3:
            difficulty_name = "Hard"
            chances = 3
            break
        else:
            print("Invalid input. Please enter an integer between 1 and 3")

    print(f"Great! You have selected the {difficulty_name} difficulty level.")


    # - If the user’s guess is correct, the game should display a congratulatory message along with the number of attempts it took to guess the number.
    # - If the user’s guess is incorrect, the game should display a message indicating whether the number is greater or less than the user’s guess.
    # - The game should end when the user guesses the correct number or runs out of chances.
    for attempt in range(chances):
        guess = int(input("Enter your guess: "))
        if guess > random_number:
            print(f"Incorrect! The number is less than {guess}.")
        elif guess < random_number: 
            print(f"Incorrect! The number is greater than {guess}.")
        else:
            print(f"Congratulations! You guessed the correct number in {attempt + 1} attempts.")
            break
    else:
        print("Game over!")

main()