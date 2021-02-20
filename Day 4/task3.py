# Task-02 - Create a Mobile class with ram and rom instance attributes.

# Author : Muhammad Turab

class Mobile:

    def __init__(self, brand_name, ram, rom):
        self.brand_name = brand_name
        self.ram = ram
        self.rom = rom

    def display_specs(self):
        return f'{self.brand_name}, {self.ram}GB RAM, {self.rom}GB ROM'


i_phone = Mobile("Iphone 7 Plus", 4, 128)

print(i_phone.display_specs())

