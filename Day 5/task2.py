# Author: Muhammad Turab
import random


class Mobile:
    def __init__(self, brand, ram, rom):
        self.brand = brand
        self.ram = ram
        self.rom = rom

    @classmethod
    def lucky_draw(cls, list):
        num = random.randint(0, len(list)-1)
        return list[num]


list = ['Nokia', 'Iphone', 'Samsung', 'Blackberry']
print(Mobile.lucky_draw(list))

