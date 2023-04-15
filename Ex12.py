import random

a = random.sample(range(30), 10)
print(a)


# Im trying to print only the first number in the list and the last
def list_sorter(a):
    print(a[:: len(a) - 1])
    # the slice function [Start:Stop:Step]
    # the Step allows the slice to step over the total length of the list -1
    # This gets to last number


list_sorter(a)
