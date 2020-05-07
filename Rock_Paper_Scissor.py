import random
import time

_list = ["Rock", "Paper", "Scissor"]
right = 0
right_computer = 0

user_name = input("What's your name? ")
print("Hello, " + user_name + "! you are now playing 3 rounds of "
                              "Rock, Paper, Scissor against the computer. " 
                              "Good luck!")

print("""Choose between:
    1. Rock
    2. Paper 
    3. Scissor""")

while right < 3 and right_computer < 3:
    try:
        choice = int(input("1 (Rock), 2 (Paper) oder 3 (Scissor)? "))
        if choice > 3 or choice <= 0:
            raise 
    except:
        print("Wrong input, only 1, 2 or 3 allowed.")
        continue

    if choice == 1:
        print("Your choice: Rock")
    if choice == 2:
        print("Your choice: Paper")
    if choice == 3:
        print("Your choice: Scissor")

    print("The computer is thinking .......")
    time.sleep(2)
    auswahl_computer = random.choices(_list)
    print("The computers choice: " + str(*auswahl_computer))
    
    if choice == 1 and auswahl_computer == ["Rock"]:
        print("Draw!")
    elif choice == 1 and auswahl_computer == ["Paper"]:
        print("You lose!")
        right_computer += 1
    elif choice == 1 and auswahl_computer == ["Scissor"]:
        print("You win!")
        right += 1

    if choice == 2 and auswahl_computer == ["Rock"]:
        print("You win!")
        right += 1
    elif choice == 2 and auswahl_computer == ["Paper"]:
        print("Draw!")
    elif choice == 2 and auswahl_computer == ["Scissor"]:
        print("You lose!")
        right_computer += 1

    if choice == 3 and auswahl_computer == ["Rock"]:
        print("You lose!")
        right_computer += 1
    elif choice == 3 and auswahl_computer == ["Paper"]:
        print("You win!")
        right += 1
    elif choice == 3 and auswahl_computer == ["Scissor"]:
        print("Draw!")

    if right < 3 and right_computer < 3:
        print("It stands " + str(right) + ":" + str(right_computer))
   
if right > right_computer:
    print("You've won " + str(right) + ":" + str(right_computer))
    print("Feel free to play another round, " + user_name + ".")
elif right_computer > right:
    print("You've lost " + str(right) + ":" + str(right_computer))
    print("Better luck next time, " + user_name + "!")
