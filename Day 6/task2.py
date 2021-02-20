# Author: Muhammad Turab

class Mobile:

    def __init__(self, brand, model, country):
        self.brand = brand
        self.model = model
        self.country = country

    @property
    def manufacture(self):
        return f"{self.brand} {self.model} was manufactured in {self.country}"


phone1 = Mobile("Iphone", "7plus", "California")
print(phone1.manufacture)
phone1.country = "China"
print(phone1.manufacture)


