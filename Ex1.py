print("Enter your name")
name = input()
print("Enter your age in years")
age = int(input())


time_till_100 = 100 - int(age)
print(name + " you will be 100 in ", time_till_100, "years")
print("Enter another number smaller than 10")
random_number = int(input())

for i in range(random_number):
    print("You'll be 100 in ", time_till_100, "years")
