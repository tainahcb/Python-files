"""
Author: Tainah Correia Barreto
Objective: Project 04 Milestone -  Word Puzzle
PC 103 / CSE 110
"""

#This guessing game contains a hidden secret word stored in a variable.
# When the program is run, the user is shown underlines for each letter of the word.

print("Welcome to WORD GUESSING GAME!")

import string

#In each iteration of the game loop, the program displays the number of underscores corresponding to the length of the secret word.
# The user is then prompted to enter their guess.

def get_hint(secret_word, guess):
    hint = ""
    for i in range(len(secret_word)):
        if secret_word[i] == guess[i]:
            hint += secret_word[i].upper()
        elif secret_word[i] in guess:
            hint += secret_word[i].lower()
        else:
            hint += "_"
    return hint

#The `play_game` function is the main game loop.
# It initializes the secret word, guess, guess count, and hint. The game continues until the user correctly guesses the secret word.

def play_game():
    secret_word = "apple"
    guess = ""
    guess_count = 0
    hint = ""

    while guess != secret_word:
        print("".join(["_"] * len(secret_word)))
        guess = input("Enter your guess: ").lower()

        if len(guess) != len(secret_word):
            print(f"The secret word has {len(secret_word)} letters. Try again.")
        else:
            hint = get_hint(secret_word, guess)
            guess_count += 1
            print(f"Hint: {hint}")

    print(f"Congratulations! You guessed the secret word in {guess_count} guesses.")

play_game()