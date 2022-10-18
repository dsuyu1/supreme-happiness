import re

# Get the answer.
answer = "What's Up, Doc?" 

# Capitalizes all the letters in the answer string.
answer = answer.upper()

# Pre-game setup.
answer_guessed = []

for current_answer_character in answer: 
    if re.search('^[A-Z]$', current_answer_character):
        answer_guessed.append(False)
    else: 
        answer_guessed.append(True)

# Game logic (memory).
num_of_incorrect_guesses = 5

current_incorrect_guesses = 0 

letters_guessed = []

# User gameplay logic. 
while current_incorrect_guesses < num_of_incorrect_guesses and False in answer_guessed:
    # Displays game stats. 
    print(f'Number of incorrect guesses remaining: {num_of_incorrect_guesses - current_incorrect_guesses}')