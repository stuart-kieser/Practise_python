num = int(input("Enter a number:"))

b = []

for divisor in range(1, num):
    if num % divisor == 0:
        b.append(divisor)
        divisor = divisor - 1

print(b)
