fib_sequence = []
x = 1
fib_sequence.append(x)
x = 1
fib_sequence.append(x)

length = int(input())
while len(fib_sequence) < length:
    x = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(x)

print(fib_sequence)
