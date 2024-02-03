class Car:
    def __init__(self, brand, model, production_year, color, horse_power, is_sport_car=False):
        self.brand = brand
        self.model = model
        self.production_year = production_year
        self.color = color
        self.horse_power = horse_power
        self.is_sport_car = is_sport_car

    def change_color(self, new_color):
        if new_color.lower() != self.color.lower():
            self.color = new_color
            return True
        else:
            return False

    def increase_horse_power(self, hp):
        if hp > 0:
            self.horse_power += hp
            return True
        else:
            return False


car1 = Car("Toyota", "Camry", 2020, "Blue", 180)


new_color = car1.change_color('blue')
print(new_color)
