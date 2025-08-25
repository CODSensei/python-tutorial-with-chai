class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fullName(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fullName(self):
        return super().fullName() + f" {self.battery_size}"


my_car = Car("BMW", "M5-CS")
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_car.fullName())
print(my_tesla.fullName())
