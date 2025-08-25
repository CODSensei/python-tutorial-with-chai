class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand

    def fullName(self):
        return f"{self.__brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, __brand, model, battery_size):
        super().__init__(__brand, model)
        self.battery_size = battery_size

    def fullName(self):
        return super().fullName() + f" {self.battery_size}"


my_car = Car("BMW", "M5-CS")
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_car.fullName())
print(my_tesla.fullName())
print(my_tesla.get_brand())
