
# Author: Muhammad Turab

class Mobile:
    def __init__(self, brand, ram, rom):
        self.brand = brand
        self.ram = ram
        self.rom = rom


class KeypadPhone(Mobile):
    def __init__(self, brand, ram, rom, touch=False):
        super().__init__(brand, ram, rom)
        self.touch = touch

    def print(self):
        return f'Brand = {self.brand}, RAM = {self.brand}, ROM = {self.rom}, Touch = {self.touch}'


keypdad = KeypadPhone("Iphone", 4, 128)

print(keypdad.print())


