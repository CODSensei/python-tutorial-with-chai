class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand

    def fullName(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "Combustion Engine Cars Sounds Good"

    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, __brand, __model, battery_size):
        super().__init__(__brand, __model)
        self.battery_size = battery_size

    def fullName(self):
        return super().fullName() + f" {self.battery_size}"

    def fuel_type(self):
        return "Electricity"


class Battery:
    def battery_info(self):
        return "this is battery"


class Engine:
    def engine_info(self):
        return "this is engine"


class ElectricShit(Battery, Engine, Car):
    pass


my_car = Car("BMW", "M5-CS")
my_tesla = ElectricCar("Tesla", "model S", "85kWh")
formulaE = ElectricShit("Mclaren", "MCL-1")

print(my_car.fullName())
print(my_car.get_brand())
print(my_car.fuel_type())
print(my_car.model)
print(isinstance(my_car, Car))
print(isinstance(my_car, ElectricCar))
print()
print(Car.total_car)
print(Car.general_description())
print()
print(my_tesla.fullName())
print(my_tesla.get_brand())
print(my_tesla.fuel_type())
print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))
print()
print(formulaE.fullName())
print(formulaE.engine_info())
print(formulaE.battery_info())
