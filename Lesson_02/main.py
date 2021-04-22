#1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
#2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
#3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
#4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
#5. Реализовать структуру "Рейтинг", представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
#6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

#1
list = ['один', 10, 2.25, [5, 15], 'пять']

for i in range(len(list)):
    print(type(list[i]))
#2
list = []
last_element_index = -1
for i in range(5):
    list.append(int(input(f'{i + 1}: ')))
i = 0
while i < len(list) - 1:
    list[i], list[i + 1] = list[i + 1], list[i]
    i += 2
    print(list)
#3
months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December',
}

print(months[int(input("Enter the month as an integer: "))])

#4
string = input("enter string: ")
list = string.split()
for i in range(len(list)):
    print(list[i][:10])

#5
list = [7, 5, 3, 3, 2]
while(True):
    print(list)
    new_element = input("press Q to exit or enter a number")
    if new_element.lower() == 'q':
        break
    new_element = int(new_element)
    last_index = -1
    for i in range(len(list)):
        if new_element == list[i]:
            last_index = i
    if last_index != -1:
        list.insert(last_index, new_element)
    elif list[0] < new_element:
        list.insert(0, new_element)
    else:
        list.append(new_element)
#6*
FIELD_NAME = "название"
FIELD_PRICE = "цена"
FIELD_QUANTITY = "количество"
FIELD_UNITS = "eд"

goods = [
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
]

analytics = {
    FIELD_NAME: [],
    FIELD_PRICE: [],
    FIELD_QUANTITY: [],
    FIELD_UNITS: [],
}

def findElement(array, required_element):
    index = -1
    for item in range(len(array)):
        if array[item] == required_element:
            index = item
    return index

while True:
    name_product = input("press Q to exit or enter name product: ")
    if name_product.lower() == 'q':
        break
    price_product = int(input("enter price product: "))
    price_quantity = int(input("enter quantity product: "))
    price_units = input("enter units product: ")
    goods.append((len(goods) + 1, {FIELD_NAME: name_product,
                                   FIELD_PRICE: price_product,
                                   FIELD_QUANTITY: price_quantity,
                                   FIELD_UNITS: price_units}))
print(goods)

for product in goods:
    product_id = findElement(analytics[FIELD_NAME], product[1][FIELD_NAME])

    if product_id != -1:
        analytics[FIELD_NAME][product_id] = product[1][FIELD_NAME]
        analytics[FIELD_PRICE][product_id] += product[1][FIELD_PRICE]
        analytics[FIELD_QUANTITY][product_id] += product[1][FIELD_QUANTITY]
    else:
        analytics[FIELD_NAME].append(product[1][FIELD_NAME])
        analytics[FIELD_PRICE].append(product[1][FIELD_PRICE])
        analytics[FIELD_QUANTITY].append(product[1][FIELD_QUANTITY])

    index = findElement(analytics[FIELD_UNITS], product[1][FIELD_UNITS])
    if index != -1:
        analytics[FIELD_UNITS][index] = product[1][FIELD_UNITS]
    else:
        analytics[FIELD_UNITS].append(product[1][FIELD_UNITS])

print(analytics)