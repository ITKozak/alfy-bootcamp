#! /usr/bin/python

import rock_paper_scissors_helper as hp

def play_round(opponent):
    current_game = [0, 0]
    match opponent:
        case "pc":
            while 3 not in current_game:
                player1, player2 = hp.user_choice(), hp.computer_choice()
                if player1 == "EXIT":
                    return 9
                current_game = hp.update_score(current_game, hp.pick_winner(player1, player2))
        case "player":
            while 3 not in current_game:
                player1, player2 = hp.user_choice(1), hp.user_choice(2)
                if "EXIT" == player1 or "EXIT" == player2:
                    return 9
                current_game = hp.update_score(current_game, hp.pick_winner(player1, player2))
    if current_game[0] == 3:
        hp.update_stats('p1')
        if opponent == 'pc':
            print('You win!')
        else:
            print("Player 1 wins!")
    else:
        if opponent == 'pc':
            hp.update_stats('pc')
            print('PC wins!')
        else:
            hp.update_stats('p2')
            print("Player 2 wins!")
    
    

def main():
    while True:
        if play_round(hp.pre_round()) == 9:
            return
        if input("Play one more round (y/n)? : ") == 'n':
            continue
    hp.print_status()
        

if __name__ == "__main__":
    main()