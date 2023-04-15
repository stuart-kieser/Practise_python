num = int(input("Enter any random number:"))

check = int(input("Input another number:"))

if num % 2 == 0:
    print("Number 1 is even")
else:
    print("Number is odd")

if num % 4 == 0:
    print(num, "is a multiple of four")

if num % check == 0:
    print("First number is divisble by second number")
