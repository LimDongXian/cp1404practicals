import random

from prac_09.car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = random.randint(0, 100)
        # print(random_number)  # for testing purpose
        if random_number < self.reliability:
            return super().drive(distance)
        else:
            return 0
