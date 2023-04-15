import random

num_guess = 1
numbers = random.randint(1, 9)
Answer = False
chosen_number = int(numbers)


def wrong():
    global num_guess
    num_guess = num_guess + 1


while Answer is False:
    user_choice = int(input("Choose a number: "))
    if user_choice < chosen_number:
        print("guess is low")
        wrong()
    if user_choice > chosen_number:
        print("guess is high")
        wrong()
    if user_choice == chosen_number:
        Answer = True
        print("you guessed it!")
        print("you made " + str(num_guess) + " guesses")
