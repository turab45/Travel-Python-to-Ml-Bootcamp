
# Author: Muhammad Turab

class Mobile:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @property
    def fullname(self):
        return f'{self.brand} {self.model}'

    @fullname.setter
    def fullname(self, name):
        brand, model = name.split(" ")
        self.brand = brand
        self.model = model

phone1 = Mobile("Iphone", "7plus")
print(phone1.fullname)
phone1.fullname = "Samsung S21"
print(phone1.fullname)



