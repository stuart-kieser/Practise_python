from datetime import datetime

user = input()
current_year = datetime.now().year

print("Hi! " + user + " how old are you now?")
age = int(input())

print("You will turn 100 in the year:", current_year - age + 100)
