from Car import Car


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'overspeeding! current speed: {self.speed}')
        else:
            print(f'current speed: {self.speed}')