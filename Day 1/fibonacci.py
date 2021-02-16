
# Author: Muhammad Turab

size = 100

# first two terms
n1, n2 = 0, 1
count = 0


if size == 1:
    print("Fibonacci sequence in range ", size, ":")
    print(n1)
else:
    print("Fibonacci sequence is :")
    while count < size:
        print(n1, end=" ")
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1


