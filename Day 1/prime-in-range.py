
# Author: Muhammad Turab

factor = 0
for i in range(0, 100):

    if (i == 1):
        continue
    factor = 1

    for j in range(2, i // 2 + 1):
        if (i % j == 0):
            factor = 0
            break

    # factor = 1 means i is prime
    # and factor = 0 means i is not prime
    if (factor == 1):
        print(i, end=" ")

