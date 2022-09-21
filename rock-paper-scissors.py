import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    # both computer and user are equal, print tie
    if user == computer:
        print("It's a tie!")

    # both computer < user are equal, print won
    elif is_win(user, computer):
        print('You won!')
    
    # both computer > user are equal, print won
    else:
      print('You lost!')

def is_win(player, computer):
    if(player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        return True

play()