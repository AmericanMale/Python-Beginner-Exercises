import random
import string

printable_characters = string.printable[:95]*10
right = 0

while right != 1:
    try:
        user_input = int(input("Choose a lenght for you password "
                               "(min. 6 and max. 50 characters): "))
        if user_input < 6 or user_input > 50:
            print("Out of range!")
            continue
        right += 1        
    except:
        print("Wrong input, only numbers between 6 and 50 are allowed.")
        
password = (random.sample(printable_characters, user_input))
final_password = random.sample(password, user_input)
final_password_as_string = " ".join(final_password).replace(" ", "")
print("Generated password for you: " + final_password_as_string)