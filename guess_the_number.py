"""This code is a simple number guessing game. It starts by asking the user to input a number to set the upper limit of the guessing range. 
If the input is valid, it generates a random number within that range. The user then repeatedly guesses the number, receiving feedback on whether their guess is too high or too low. 
This process continues until the user correctly guesses the number, at which point the game congratulates them and displays the total number of attempts made."""

import random

top_of_range = input("Type a number that you want to make the top of the range : ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("Your guess was above the number!")
    else:
        print("Your guess was below the number!")

print("You got it in", guesses, "guesses")
