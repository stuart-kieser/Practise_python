a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for num in list(a) and list(b):
    if num in list(a) and list(b):
        c.append(num)
print(c)

print([num for num in a if num in b])
print(set(a) & set(b))
