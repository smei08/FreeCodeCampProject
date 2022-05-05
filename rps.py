#game of rock paper and sissors

import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for sissor\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'it\'s a tie!\n' + 'computer choice: ' + computer

    if is_win(user, computer):
        return'you won!\n' + 'computer choice: ' + computer

    return 'you lost!\n' + 'computer choice: ' + computer


def is_win(player, opponent):
    #returns true if player wiins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True
    
print(play())