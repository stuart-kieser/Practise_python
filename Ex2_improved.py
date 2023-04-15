num = int(input("Input number:"))

if num % 2 == 0:
    print(f"{num}", "is even")
    if num % 4 == 0:
        print(f"{num}" " is a multiple of 4")

else:
    print(f"{num}", "is odd")
