# cows and bulls
# this is the github test, lets see if this works
import random

store_num = []
guessed_num = []


for number in range(4):
    random_number = random.randint(0, 9)
    store_num.append(random_number)

print(store_num)

guesses = 0

while True:
    guess = int(input("Guess a number in the field: "))
    guesses = guesses + 1
    if guess in store_num:
        print("Thats a cow")
        guessed_num.append(guess)
    else:
        print("thats a bull! Try again.")

    if set(guessed_num) == set(store_num):
        print("You guessed it!")
        print("You made ", guesses, "guesses")
        break
