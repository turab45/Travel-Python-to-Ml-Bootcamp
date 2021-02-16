
# Author: Muhammad Turab
sum_of_even = 0
sum_of_odd = 0

for i in range(0, 101):
    if i % 2 == 0:
        sum_of_even += i
    else:
        sum_of_odd += i

print("Sum of all even = ", sum_of_even)
print("Sum of all odd = ", sum_of_odd)


