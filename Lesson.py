class Heart:
    def __init__(self, load):
        self.load = load

    def state(self):
        return "bad blood" if self.load > 70 else "feeling good"


class Brain:
    def __init__(self, load):
        self.load = load

    def state(self):
        return "tired" if self.load > 90 else "rested"


class Leg:
    def __init__(self, moving_speed):
        self._moving_speed = moving_speed

    @property
    def movement_state(self):
        return "running" if self._moving_speed > 10 else "walking" if self._moving_speed > 0 else "standing"


class Person:
    def __init__(self, heart_load, brain_load):
        self.heart = Heart(heart_load)
        self.brain = Brain(brain_load)


    def attach_leg(self, leg_instance):
        self.leg = leg_instance



heart_load = 75
brain_load = 85
leg_speed = 12

person = Person(heart_load, brain_load)
leg_instance = Leg(leg_speed)
person.attach_leg(leg_instance)

print(f"Heart State: {person.heart.state()}")
print(f"Brain State: {person.brain.state()}")
print(f"Leg Movement State: {person.leg.movement_state}")
