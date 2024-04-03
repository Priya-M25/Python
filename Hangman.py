'''
Output :-
Welcome to Hangman!

_ _ _ _ _

Sorry, 'g' is not in the word.

_ _ _ _ _

Good guess! 'a' is in the word.

a_ _ _ _

Good guess! 'p' is in the word.

app_ _

Good guess! 'l' is in the word.

appl_

Good guess! 'e' is in the word.

Congratulations! You've guessed the word: apple

'''

import random

def choose_random_word():
    word_list = ["apple", "banana", "cherry", "date", "grape", "orange", "pear"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def hangman():
    max_attempts = 6
    word_to_guess = choose_random_word()
    guessed_letters = []
    attempts = 0
    
    print("Welcome to Hangman!")
    
    while True:
        print(display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word_to_guess:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts += 1
        
        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"Congratulations! You've guessed the word: {word_to_guess}")
            break
        
        if attempts >= max_attempts:
            print(f"Sorry, you've run out of attempts. The word was '{word_to_guess}'.")
            break

if __name__ == "__main__":
    hangman()
