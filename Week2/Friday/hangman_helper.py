#! /usr/bin/bash

# We use choices to get random list from imported list of words.
from random import choices
from os import path
import sys
# Declaration of consts.
HINTS = 0
INITIAL_POINTS = 10
# We use "constant" list of words, which we append only once while openning words.txt.
WORD_LIST = list()

# Globall variables for ingame usage
player_score = INITIAL_POINTS
guesses = 1
played_games = 0


def get_random_word(words: list) -> str:
    '''Pick and return random word from provided list.'''
    return choices(words)[0]

def get_hint(word: str, pattern: str, ) -> str:
    '''Based on guessed letter return hint which is a single letter which still hiden.
    
    We sort hiden word and check if letter in oppened letters from pattern and if that letter appearce
    only once in word . Sorting letters prevent any additional hints about location of letter in the word.'''
    if pattern.count("_") == 1:
        return "Cmon, It's the last letter. I believe in you!"
    hint_letters = list(word)
    hint_letters.sort()
    for l in hint_letters:
        if l not in pattern and word.count(l) < 2:
            return l
    # If we couldn't provide hint - return text.
    return "Sorry, no more hints for you."

# TODO combine both list coperhension in
def filter_words_list(pattern: str, wrong_guess_list: list, words: list=WORD_LIST) -> list:
    '''The function returns a new list that contains only the words in the list of words that match the pattern and the previous guesses.'''
    # I'm proud of it, dont kill me pls.

    # Declare list of hints which we'll be updating and returning.
    hints_list = list()
    for word in words:
        # If len of word and pattern is diffetent - this couldnt be our hint.
        if len(word) == len(pattern): 
            # Here we checking if letters from wrong list in potential hint.
            # If it does - this word couldn't be our hint.
            if [char for char in wrong_guess_list if char in word]:
                continue
            # Here we checking if potential hint have the same placement of known letters in pattern.
            # If they are different - this word couldn't be out hint
            if [True for i in range(len(word)) if pattern[i] != "_" and pattern[i] == word[i]]:
                continue
            # If previous checks dosent trigger - we add current word as a hint.
            hints_list.append(word)
    return hints_list

def state_display(pattern: str, score: int, guesses: list, extras: str='') -> None:
    '''Print current state of the game.'''
    print(f"""\
Current pattern: {pattern}
Current points: {score}
Wrong guesses: {"|".join(guesses)}""")
    if extras != '':
        print(extras)

def get_input() -> list:
    '''Get user input and return it.'''
    user_input = input("Enter '!word' to guess a word, '?' to get a hint, or just type a letter to guess: ")
    if user_input == "?":
        return "HINT", None
    elif user_input[0] == "!":
        return "WORD", user_input[1:].lower()
    elif user_input.isalpha() and len(user_input) == 1:
        return "LETTER", user_input.lower()

def word_loader(file_name="words.txt") -> list:
    '''Open file with words, parse then and return list of words.'''
    words_list = []
    # Using witth as a more robust solution.
    with open(path.join(sys.path[0], file_name), 'r') as f:
        for line in f:
            word = line.strip()
            if(word.isalpha()):
                words_list.append(word)
    return words_list

def play_again(msg: str) -> bool:
    """Prints the message to the player, and gets input from him if she wants to play again."""
    print(msg)
    print("Enter 'Y' or 'y' for YES, 'N' or 'n' for NO:")
    while True:
        choice = input()
        if choice and choice[0] in 'yY':
            return True
        if choice and choice[0] in 'nN':
            return False

def end_of_the_game(score: int, word: str=None) -> None:
    '''Prints final result and win\lose status.'''
    if score > 0:
        print(f'''\
Congratulations! You won!
Are {word} was too easy for you?''')
        return
    print(f'''\
You lost. Better luck next time!
Btw, correct answer is - {word}.''')

WORD_LIST = word_loader()
