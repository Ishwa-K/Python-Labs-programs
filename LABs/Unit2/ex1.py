#Number guessing game.
import random

number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

while guess != number:
    print("Wrong guess! Try again.")
    guess = int(input("Enter your guess: "))

print("Congratulations! You guessed the correct number.")