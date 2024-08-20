import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game!\n")
print("I'm thinking of a number between 1 and 100.\n")

chosen_number = random.randrange(1, 100)
game_on = True

mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
if mode == "easy":
    lives = 10
else:
    lives = 5

while game_on:
    print(f"You have {lives} attempts remaining to guess the number.")

    if lives != 0:
        guess = int(input("Make a guess: "))
        if guess != chosen_number:
            if guess > chosen_number:
                print("Too high.")
            elif guess < chosen_number:
                print("Too low.")
        else:
            game_on = False
            print(f"You got it! The answer was: {chosen_number}")

    else:
        game_on = False
        print(f"You ran out of attempts. The answer was: {chosen_number}")
    lives -= 1