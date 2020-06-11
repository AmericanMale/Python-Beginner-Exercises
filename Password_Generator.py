from random import sample
from string import printable

printable_characters = printable[:95]*10

while True:
    try:
        user_input = int(input("Choose a lenght for you password "
                               "(min. 6 and max. 50 characters): "))
        if user_input < 6 or user_input > 50:
            raise ValueError
            continue        
    except ValueError:
        print("Wrong input, only numbers between 6 and 50 are allowed.")
        
password = (sample(printable_characters, user_input))
final_password = sample(password, user_input)
final_password_as_string = " ".join(final_password).replace(" ", "")
print("Generated password for you: " + final_password_as_string)
