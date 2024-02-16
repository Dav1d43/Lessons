class Vehicle:
    def start_engine(self):
        pass

    def stop_engine(self):
        pass

class Car(Vehicle):
    def __init__(self, max_speed):
        self.max_speed = max_speed
        self.current_speed = 0

    def start_engine(self):
        return "car started"

    def stop_engine(self):
        self.current_speed = 0
        return "car stopped"

class SportCar(Car):
    def start_engine(self):
        parent_start_result = super().start_engine()
        print(f"{parent_start_result}, max speed: {self.max_speed}")

    def stop_engine(self):
        parent_stop_result = super().stop_engine()
        print(f"{parent_stop_result}, current speed: {self.current_speed}")

# Example usage:
car = SportCar(max_speed=200)
car.start_engine()
car.stop_engine()
