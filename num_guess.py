# Author: Erik Blackowicz
# Date: 7/6/20
# Description: Code will ask the user for an integer, then the user will try to guess said integer. If the guess is too high or too low it will
# prompt the user to guess again. When the number is guessed correctly, the program will tell the user how many attempts they used to reach a sucessful guess.

answer = int(input("Enter the number for the player to guess.\n"))
count = 1                       # must be 1, if 0 will be incorrect by -1 guess.
print("Enter your guess.")
while True:
    guess = int(input())
    if guess == answer and count == 1:  # first priority for 1st correct guess
        print("You guessed it in 1 try.")
    elif guess < answer:
        print("Too low - try again:")
    elif guess > answer:
        print("Too high - try again:")
    else:
        print("You guessed it in " + str(count) + " tries.")
        break
    count = count + 1       # counter is used to track the # of guesses, unless 1st guess correct
