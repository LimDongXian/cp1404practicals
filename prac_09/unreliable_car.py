import random

from prac_09.car import Car


class UnreliableCar(Car):
    """A car that has a chance to fail driving based on its reliability."""
    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar with a name, fuel, and reliability."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive a distance, depending on reliability."""
        random_number = random.randint(0, 100)
        # print(random_number)  # for testing purpose
        if random_number < self.reliability:
            return super().drive(distance)
        else:
            return 0
