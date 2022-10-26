import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = [''] * len(self.word)
        self.num_letters = [1 for i in list(set(self.word)) if i not in self.word_guessed]
        self.list_of_guesses = []

test = Hangman(['apple'])
print(test.word_guessed)
