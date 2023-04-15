import random


def create_list():
    data_set = []
    for num in data:
        if num not in data_set:
            data_set.append(num)
    return data_set


def create_set():
    return list(set(data))


data = [2, 4, 6, 3, 5, 7, 9, 7, 5, 3, 54, 3, 2, 43, 56, 8, 9]

print(create_list())
print(create_set())
