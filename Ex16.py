import random


def password_generator():
    x = int(input("How long would you like your password to be? "))
    characters = "1234567890qwertyuiopasdfghjklzxcvbnm"
    password = "\n".join(random.sample(characters, x))
    return print(password)


password_generator()
