from OfficeEquipment import OfficeEquipment


class Xerox(OfficeEquipment):
    def __init__(self, width, height, copy_speed):
        super().__init__(width, height)
        self.copy_speed = copy_speed