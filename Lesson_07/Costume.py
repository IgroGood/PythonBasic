from Clotches import Clothes


class Costume(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def tissue_consumption(self) -> int:
        return self.height + 0.3
