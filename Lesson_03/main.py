#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
#4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
#5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
#6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
#Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


# 1
input_number_1 = int(input("a: "))
input_number_2 = int(input("b: "))

def division(num_1, num_2):
    if num_2 != 0:
        return num_1 / num_2
    return

print(division(input_number_1, input_number_2))


# 2
user_name = input("Enter your username: ")
user_soname = input("Enter the last name of the user: ")
user_year = input("Enter the user's year of birth: ")
user_city = input("Enter the user's city: ")
user_email = input("Enter user e-mail: ")
user_tel = input("Enter user phone: ")

def print_user_data(name, soname, year, city, email, tel):
    print(f'{name}, {soname}, {year}, {city}, {email}, {tel}')

print_user_data(name=user_name,
                soname=user_soname,
                year=user_year,
                city=user_city,
                email=user_email,
                tel=user_tel)


# 3
number_1 = int(input("a = "))
number_2 = int(input("b = "))
number_3 = int(input("c = "))

def my_func(*inputs):
    inputs = list(inputs)
    sum = 0
    for args in range(2):
        number_max = max(inputs)
        sum += number_max
        inputs.remove(number_max)
    return sum

print(my_func(number_1, number_2, number_3))


#4
input_x = float(input("Введите действительное положительное число х: "))
input_y = int(input("Введите целое отрицательное число y: "))

def my_func(x, y):
    return x ** y

print(my_func(input_x, input_y))

def my_func_2(x, y):
    result = x
    for i in range(y - 1):
        result *= x
    return result

print(my_func_2(input_x, input_y))


#5
def get_sum():
    numbers_sum = 0
    while True:
        user_input = input("Enter a string of numbers separated by a space: ")
        user_numbers = user_input.split(" ")
        for i in range(len(user_numbers)):
            if user_numbers[i].isdigit():
                numbers_sum += int(user_numbers[i])
            else:
                return numbers_sum
            print(numbers_sum)

get_sum()


#6
def int_func(word):
    return word.capitalize()

def make_words_title():
    user_input = input("Eater string: ")
    data_list = user_input.split(" ")
    result_string = ""
    for words in data_list:
        result_string += int_func(words) + " "
    return result_string

print(make_words_title())
