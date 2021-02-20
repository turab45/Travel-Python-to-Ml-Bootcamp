# Task-02 - Create a Mobile class with ram and rom instance attributes.

# Author : Muhammad Turab

class Mobile:

    def __init__(self, brand_name, ram, rom):
        self.brand_name = brand_name
        self.ram = ram
        self.rom = rom


i_phone = Mobile("Iphone", 4, 128)

print(i_phone.brand_name, i_phone.ram, i_phone.rom)


