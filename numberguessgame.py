import random

secret_number = random.randint(1, 100)

guess = None
attemps = 0


while guess != secret_number:
    guess = int(input("Guess a number between 1 and 100 ::"))

    attemps += 1
    if guess > 100:
        print("you are not allowed put greater than 100")
    elif guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    elif guess > 100:
        print("you are not allowed put after 100")
    else:
        print(f"You guessed it right, and the attemps are :{attemps}")
