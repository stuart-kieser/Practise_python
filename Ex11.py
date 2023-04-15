num = int(input("Input any number "))
rand_int = 2

for rand_int in range(2, num):
    if num % rand_int == 0:
        print("Number is not a prime")
        break

else:
    print("Prime")
