

# Muhammad Turab

number = 9
i = 1
factor = 0
while number >= i:
    if number % i == 0:
        factor = factor + 1
    i = i+1


if factor == 2 or factor == 1:
    print(number, " is a prime number")
else:
    print(number, " is not a prime number")


