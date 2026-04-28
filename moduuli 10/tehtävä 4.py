import random

class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print(f"Race: {self.name}")
        print(f"{'License plate':<15} {'Speed (km/h)':>12} {'Distance (km)':>13}")
        print("-" * 42)
        for car in self.cars:
            print(f"{car.license_plate:<15} {car.current_speed:>12} {car.travelled_distance:>13}")

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)