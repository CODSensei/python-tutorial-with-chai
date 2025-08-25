# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fullName(self):
        return f"{self.brand} {self.model}"


my_car = Car("BMW", "M5-CS")
print(my_car.fullName())
