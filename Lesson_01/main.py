# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
#
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.


import time

#1
integer_value = int(input('Enter your integer value:'))
float_value = float(input('Enter your float value:'))
boolean_value = bool(input('Enter your boolean value:'))
string_value = input('Enter your string value:')

print(f'integer_value: {integer_value}')
print(f'float_value: {float_value}')
print(f'boolean_value: {boolean_value}')
print(f'string_value: {string_value}')

#2
time_in_seconds = int(input('Enter time in seconds:'))
print(time.strftime('%H:%M:%S', time.localtime(time_in_seconds)))

#3
number = int(input('Enter your integer value:'))
#print(number * 100 + number * 10 + number)
print(str(number)*3)

#4
number = int(input('Enter your integer value (n > 0):'))
max_number = 0
while number > 0:
    current_value = number % 10
    if current_value > max_number:
        max_number = current_value
    number //= 10
print(max_number)

#5
revenue_values = float(input('revenue_values:'))
company_costs = float(input('company_costs:'))

if revenue_values > company_costs:
    print("the company is working in a plus")
    profit = revenue_values - company_costs
    print(f'profit: {profit}')
    number_of_employees = int(print("enter the number of employees"))
    profit_per_employee = profit / number_of_employees
    print(f'profit_per_employee: {profit_per_employee}')
else:
    print("the company is working in a minus")

#6
result_first_day = 2
desired_result = 3

current_result = result_first_day
current_day = 1
while current_result < desired_result:
    current_result *= 1.1
    current_day += 1
print(current_day)
