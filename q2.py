class Vehicle:
    def __init__(self, name, v_speed, manufacturer):
        self.name = name
        self.v_speed = v_speed
        self.manufacturer = manufacturer

    def speed(self):
        return print(f'The speed is {self.v_speed} kmh')


class Car(Vehicle):
    def __init__(self, horsepower=1176, name='Koenigsegg Agera RS', v_speed=447.19, manufacturer='Koenigsegg'):
        super().__init__(name, v_speed, manufacturer)
        self.horsepower = horsepower


class Plane(Vehicle):
    def __init__(self, engines='Rocket engine', name='NA-X15', v_speed=7274.235, manufacturer='USAF/NASA'):
        super().__init__(name, v_speed, manufacturer)
        self.engines = engines
