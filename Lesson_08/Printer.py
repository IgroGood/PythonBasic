from OfficeEquipment import OfficeEquipment


class Printer(OfficeEquipment):
    def __init__(self, width, height, amount_of_paint):
        super().__init__(width, height)
        self.amount_of_paint = amount_of_paint
