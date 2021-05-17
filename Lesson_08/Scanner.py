from OfficeEquipment import OfficeEquipment


class Scanner(OfficeEquipment):
    def __init__(self, width, height, definition):
        super().__init__(width, height)
        self.definition = definition