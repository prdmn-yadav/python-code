import random

random_number = random.randint(1, 10)
tries = 1

name = input("Hello, What's your Name..?")

print("Hello", name + ",", )

question = input("Would you Like To Play A Game ? [Yes/No] ")

if question == "no":
    print("Ok no problem..!")

if question == "yes":

    print("I'm Thinking of a Number Between 1 & 10")
    guess = int(input("Guess a number..."))
    if guess > random_number:
        print("You are guessing to high")
    if guess < random_number:
        print("You are guessing to low")

    while guess != random_number:
        tries += 1
        guess = int(input("Try Again : "))
        if guess < random_number:
            print("Guess Higher...")
    if guess == random_number:
        print("You're Right! you win! The Number Was", random_number, "and it only in", tries, "tries!")
