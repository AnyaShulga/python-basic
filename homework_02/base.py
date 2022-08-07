from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = None
    started = False
    fuel = None
    fuel_consumption = None

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError
        return self.started

    def move(self, distance):
        if self.fuel/self.fuel_consumption >= distance:
            self.fuel -= self.fuel_consumption*distance
            return self.fuel
        else:
            raise NotEnoughFuel
