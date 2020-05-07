import random

range = 1, 20
random_number = random.randint(*range)
guess = 0
tries = 0

user_name = input("What's your name? ")
print("Hello, " + user_name + ".")
print("Guess the number between 1 und 20")

while guess != random_number:
    tries += 1
    try:
        user_input = int(input("Enter your guess: "))
    except:
        print("Wrong input, only numbers are allowed.")
        continue
    if user_input == random_number:
        print("That's the number!")
        break
    elif user_input < range[0] or user_input > range[1]:
        print("Your number is out of range!")
    elif user_input < random_number:
        print("Your number is too low.")
    elif user_input > random_number:
        print("Your number is too high.")
        
print("You have guessed the right number after " + str(tries) + " tries, " + user_name + ".")