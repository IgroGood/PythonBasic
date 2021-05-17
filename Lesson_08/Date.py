from datetime import datetime


class Date:
    @classmethod
    def __init__(cls, date: str):
        cls.date = date

    @classmethod
    def extract_date(self):
        datetime_object = datetime.strptime(self.date, '%d%m%Y')
        return datetime_object.day, datetime_object.month, datetime_object.year

    def __is_int(n):
        return int(n) == float(n)

    @staticmethod
    def validate_number(day, month, year):
        if Date.__is_int(day) and day > 0 and day < 32:
            if Date.__is_int(month) and month > 0 and day < 12:
                if Date.__is_int(year) and year >= 0:
                    return True
        return False
