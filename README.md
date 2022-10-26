# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

The entire code is written in Python.

## Milestone 2
Basic Python commands implemented to write a programme to check the user input is a single albhabetic character.


## Milestone 3
This code is an extension of the previous code, with the key change being a continuous loop for the user input until the condition is satisfied.

The function to run checks takes a guessed word as an argument. It then checks whether the lowercased letter is in in the "word". 

```python
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
```

The function asking for an input asks for a user input until the right format is received - i.e. alphabetic letter, and subsequently calls "check_guess" function to check if the letter is in the word.

```python
def ask_for_input():
    while True:
        guess = input("Please guess a letter")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)
```

