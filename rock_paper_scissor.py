import random

def play():
    user=input("'r' for rock 'p' for paper 's' for scissors ")
    computer=random.choice(['r','p','s'])

    if user==computer:
        return('tie')
    if is_win(user,computer):
        print(f"you won as i guessed {computer}")
    else:
        print(f"i won because i guessed {computer}")
    
def is_win(player,opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    
play()

        
