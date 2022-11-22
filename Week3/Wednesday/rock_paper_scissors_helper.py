#!/usr/bin/python

from random import choice

PICKS = ['r', 'p', 's']
picks = ['rock', 'paper', 'scissors']
game_data ={
    'games': 0,
    'p1': 0,
    'p2': 0,
    'pc': 0
}


def print_status():
    print(f'''\
Games played: {game_data['games']}
Player 1 wins: {game_data['p1']}
Player 2 wins: {game_data['p2']}
Computer wins: {game_data['pc']}
    ''')

def computer_choice() -> str:
    '''Return random choice for computer pick.'''
    return choice(PICKS)[0]

def user_choice(user: str='') -> str:
    input_text = ''
    if user:
        input_text = f"Player {user} "
    input_text += '''\
Make you'r pick!
Rock? Paper? Scissors?
You could also type the first letter for short variant.
Type ? if you want to look at stats.
Type ! if you want to quit.'''
    while True:
        user_input = input(input_text).lower()
        if user_input[0] in PICKS:
            return user_input[0]
        elif user_input == '?':
            print_status()
        elif user_input == '!' and input("Are you really want to quite?").lower()[0] == 'n':
            return "EXIT"
        else:
            print("Invalid input. Try again.")

def pick_winner(a_pick: str, b_pick: str) -> int:
    '''Functions takes picks of both players and return -1 as a win for first player, 1 as a win for second player'''
    winner =  PICKS.index(a_pick) - PICKS.index(b_pick)
    a_pick = picks[PICKS.index(a_pick)]
    b_pick = picks[PICKS.index(b_pick)]
    print(f" p1 - {a_pick} vs {b_pick} - p2")
    match winner:
        case 2:
            return -1
        case -2:
            return 1
        case _:
            return winner

def update_score(score: list, winner):
    if winner == -1:
        score[1] += 1
    elif winner == 1:
        score[0] += 1
    print(f"{score[0]} : {score[1]}")
    return score

def pre_round() -> str:
    while True:
        user_input = input("Pick your opponent. Type 'pc' to play against pc and 'payer' to play against another player - ").lower()
        if user_input in ['player', 'pc']:
            return user_input

def update_stats(user: str):
    game_data['games'] += 1
    game_data[user] += 1

def main():
    pass

if __name__ == "__main__":
    main()