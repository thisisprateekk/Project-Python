import random
def guessit(x):
    print("okay! let me guess the number")
    computer_guess=random.randint(1,10)
    while computer_guess != x:
        guess=input(f"is {computer_guess} too high (H) or too low (L)")
        if guess=='L':
            computer_guess=random.randint(computer_guess+1,10)
        if guess=='H':
            computer_guess=random.randint(1,computer_guess-1)
    print(f'i got it,its {x}')

guessit(4)


                


        
