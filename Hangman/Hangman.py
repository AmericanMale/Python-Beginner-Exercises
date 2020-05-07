import random
import string

numbers = string.digits
wrong = 0
right = 0

with open("sowpods.txt", "r") as file:
    data = file.read().splitlines()

word = random.choices(data)
word_string = " ".join(word)
word_length = len(word_string)
word_hidden = word_length*"_"

print("Welcome to Hangman.")
print("The game is lost with the sixths wrong guess. Good luck!")
print("The word: " + word_hidden)

guessed_word = []
_list = []

while wrong < 6 and right < word_length:
    try:
        a = input("Guess a letter: ").upper()
        if a in numbers or len(a) > 1 or a in _list:
            raise
        _list += a
        if a in word_string:
            word_letter_count = word_string.count(a)
            print("The letter " + a + " is included.")
            for w in word_string:
                if w != a and w not in _list:
                    w = "_"
                guessed_word += w
            print(*guessed_word[-word_length:])
            right += word_letter_count
        else:
            print("The word doesn't contain letter " + a)
            wrong += 1
    except:
        if a in numbers:
            print("Numbers are not allowed.")
        elif len(a) > 1:
            print("Only one letter at a time.")
        elif a in _list:
            print("You tried this letter already.")

if right == word_length:
    right += wrong
elif wrong == 6:
    wrong += right

if right > wrong:
    print("Congratulations, you have won!")
elif right < wrong:
    print("You have lost. Better luck next time!")
    print("The word: " + word_string)

