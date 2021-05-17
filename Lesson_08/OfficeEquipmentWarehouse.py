from OfficeEquipment import OfficeEquipment
import re


class OfficeEquipmentWarehouse:
    def __init__(self):
        self.__departments = dict()

    def add_departments(self, name):
        self.__departments[name] = list()

    def add_office_equipment(self, department, officeEquipment: OfficeEquipment):
        self.__departments[department].append(officeEquipment)

    def get_statistics(self, department):
        result = dict()
        id = 0
        for i in range(len(self.__departments[department])):
            if result.get(re.sub(r'[clas<>\'\s]|\..+','', f'{type(self.__departments[department][i])}')):
                result[re.sub(r'[clas<>\'\s]|\..+','', f'{type(self.__departments[department][i])}')] += 1
            else:
                result[re.sub(r'[clas<>\'\s]|\..+', '', f'{type(self.__departments[department][i])}')] = 1
        return result

    def __str__(self):
        return self.__departments.__str__()
