from Clotches import Clothes


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def tissue_consumption(self) -> int:
        return self.size/6.5+0.5