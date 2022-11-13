#! /usr/bin/python

import hangman_helper as hh

def update_word_pattern(word: str, pattern: str, letter: str) -> str:
    '''Return updated string with revealed letter.'''
    # Itterating through word to find letter. When we find one - update pattern.
    pattern = list(pattern)
    for e in range(len(word)):
        if word[e] == letter:
            pattern[e] = letter
    return ''.join(pattern)

def run_single_game(words: list, score: int) -> int:
    '''Function run signle round of the game, by picking rundom word from provided list.
    At the end returns players score.'''
    word = hh.get_random_word(words)
    pattern = "_" * len(word)
    incorrect_guesses = []
    extra_msg = ''
    while "_" in pattern and score > 0:
        hh.state_display(pattern, score, incorrect_guesses, extra_msg)
        extra_msg = ''
        guess = hh.get_input()
        match guess[0]:
            case "LETTER":
                if guess[1] in word:
                    pattern = update_word_pattern(word, pattern, guess[1])
                    points = word.count(guess[1])
                    # Here Im changing score only when we guess more than 1 letter.
                    # Othervise we don't need to add and remove 1 point.
                    if points >= 2:
                        score +=  (points * (points + 1) // 2) - 1
                else:
                    score -= 1
                    if guess[1] not in incorrect_guesses:
                        incorrect_guesses.append(guess[1])
                continue
            case "WORD":
                if guess[1] == word:
                    points = pattern.count("_")
                    score += (points * (points + 1) // 2) - 1
                else:
                    score -= 1 * hh.guesses
                    hh.guesses += 1
                continue
            case "HINT":
                hint_letter = hh.get_hint(word, pattern)
                if len(hint_letter) == 1:
                    extra_msg = f"Try this one - {hint_letter}"
                    score -= hh.HINTS
                    hh.HINTS += 1
                else:
                    extra_msg = hint_letter
                continue
            case _:
                continue
    hh.end_of_the_game(score, word)
    return score

def main():
    while hh.player_score > 0:
        if hh.played_games == 0:
            hh.player_score = run_single_game(hh.WORD_LIST, hh.player_score)
        else:
            hh.player_score += run_single_game(hh.WORD_LIST, hh.player_score)
        hh.played_games += 1
        if hh.player_score == 0: 
            if hh.play_again("You loose. Do you want to play again?"):
                hh.player_score = hh.INITIAL_POINTS
                hh.played_games = 0
                hh.HINTS = 1
            else:
                return
        elif not hh.play_again("You win. Do you want to play again?"):
            return

if __name__ == "__main__":
    main()