import time


class TrafficLight(object):
    __color = ''
    def get_color(self):
        return self.__color
    def running(self):
        __color = 'red'
        print(__color)
        time.sleep(7)
        __color = 'orange'
        print(__color)
        time.sleep(2)
        __color = 'green'
        print(__color)
        time.sleep(4)
        __color = ''
        print(__color)
        pass