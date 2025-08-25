class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand

    def fullName(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self, __brand, model, battery_size):
        super().__init__(__brand, model)
        self.battery_size = battery_size

    def fullName(self):
        return super().fullName() + f" {self.battery_size}"

    def fuel_type(self):
        return "Electricity"


my_car = Car("BMW", "M5-CS")
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_car.fullName())
print(my_car.get_brand())
print(my_car.fuel_type())
print(my_tesla.fullName())
print(my_tesla.get_brand())
print(my_tesla.fuel_type())
