from Car import Car


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'overspeeding! current speed: {self.speed}')
        else:
            print(f'current speed: {self.speed}')