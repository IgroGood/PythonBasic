# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
#
# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.


import random
import re
import json
from functools import reduce
from typing import Final


#1
f = open('1.txt', 'w+')
while True:
    text = input(": ")
    if text == '':
        break
    f.write(f'{text}\n')
f.close()
#2
with open('2.txt', encoding='utf-8') as f:
    count_words = 0
    count_lines = 0
    while True:
        line = f.readline()
        if not line: break
        count_words += len(line.split())
        count_lines += 1
        print(line, end='')
print(f'count words: {count_words}, count lines: {count_lines}')
#3
PRICE: Final = -1
their_salary = 0
amount_of_workers = 0
with open('3.txt', encoding='utf-8') as f:
    while True:
        line = f.readline().split()
        if not line: break
        their_salary += int(line[PRICE])
        amount_of_workers += 1
        if int(line[PRICE]) < 20000:
            print(" ".join(line))
print(f'their_salary: {their_salary/amount_of_workers}')

#4
vocabylary_en = {'One': 1,
              'Two': 2,
              'Three': 3,
              'Four': 4,
              'Five': 5,
              'Six': 6,
              'Seven': 7,
              'Eight': 8,
              'Nine': 9,
              'Teen': 10}

vocabylary_ru = {'Один': 1,
              'Два': 2,
              'Три': 3,
              'Четыре': 4,
              'Пять': 5,
              'Шесть': 6,
              'Семь': 7,
              'Восемь': 8,
              'Девять': 9,
              'Десять': 10}

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

with open('4a.txt', 'r', encoding='utf-8') as f:
    with open('4b.txt', 'w+', encoding='utf-8') as f2:
        while True:
            line = f.readline()
            if not line: break
            number = int(''.join(line.split()).split('—')[1])
            f2.write(f'{get_key(vocabylary_ru, number)}\n')
#5
with open('5.txt', 'w+', encoding='utf-8') as f:
    for i in range(100):
        f.write(f'{random.randint(0, 10)} ')
with open('5.txt', 'r', encoding='utf-8') as f:
    print(reduce(lambda a,b: a + b, list(map(int, f.readline().split()))))

#6
academic_subjects = {}

with open('6.txt', 'r', encoding='utf-8') as f:
    for i in f.read().split('\n'):
        academic_subject = i.split(':')
        academic_subjects[academic_subject[0]] = reduce(lambda a, b: a + b,
                                            map(lambda i: int(re.sub("\D", "", i)) if re.sub("\D", "", i) else 0,
                                                academic_subject[1].split()))
print(academic_subjects)

#7
average_profit = 0
company_list = {}
with open('7a.txt', 'r', encoding='utf-8') as f:
    while True:
        company = f.readline().split()
        if not company: break
        profit = int(company[2]) - int(company[3])
        if profit > 0:
            average_profit = (profit + average_profit) / 2
        company_list[company[0]] = profit

with open('7b.txt', 'w+', encoding='utf-8') as f:
    f.write(json.dumps(company_list))
print(f'average_profit: {average_profit}')
