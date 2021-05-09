class Road(object):
    __length = 0
    __width  = 0
    __mass_of_asphalt = 0
    __blade_thickness = 0
    def __init__(self, length, width, mass_of_asphalt, blade_thickness):
        self.__length = length
        self.__width = width
        self.__mass_of_asphalt = mass_of_asphalt
        self.__blade_thickness = blade_thickness
    def calculating_the_mass_of_asphalt(self):
        return self.__length * self.__width * self.__mass_of_asphalt * self.__blade_thickness
