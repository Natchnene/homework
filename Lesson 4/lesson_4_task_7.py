# С клавиатуры вводится натуральное число. Найти его наибольшую цифру.
# Например, введено число 764580. Наибольшая цифра в нем 8.

number = input('Введите натуральное число: ')
number_list = list(number)
number_list.sort()
print(int(number_list[-1]))