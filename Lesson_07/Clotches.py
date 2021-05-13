from abc import abstractmethod


class Clothes:
    def __init__(self, name):
        self.name = name


    @abstractmethod
    def tissue_consumption(self) -> int:
        pass