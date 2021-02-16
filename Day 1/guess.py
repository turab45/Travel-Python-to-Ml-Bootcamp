
# Muhammad Turab

import random
random_number = random.randint(1, 9)

while True:
    user_number = int(input("Enter a guess (1-9): "))
    if user_number == random_number:
        print("Well guessed!")
        break
    else:
        continue

