# Task-01 - Create a class method change_total and change value of total_phones to 5.
#Output:
#0
#5

# Author : Muhammad Turab

class Mobile:

    total_phones = 0

    @classmethod
    def change_phones(cls, phones):
        cls.total_phones = phones

    def __init__(self, brand, ram, rom):
        self.brand = brand
        self.ram = ram
        self.rom = rom
        Mobile.total_phones += 1


print(Mobile.total_phones)
Mobile.change_phones(5)
print(Mobile.total_phones)

