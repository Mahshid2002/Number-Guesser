# this program is a game that you make a guess and the computer say if it is true or not
import random 
top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger than 0. ")
        quit()
else:
    print("Pleas type a number. ")
    quit()

random_number = random.randrange(top_of_range)   # generat random number from 0 to top of range

guesses = 0

while True:
    guesses  += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Pleas type a number.")
        continue
    if user_guess == random_number:
        print("Yay! you got it.")
        break
    elif user_guess > random_number:
            print("type lower")
    else:
        print("type upper")

# This:    print("You got it in " + str(guesses) + " guesses")   or:
print("you got it in" , guesses , "guesses")