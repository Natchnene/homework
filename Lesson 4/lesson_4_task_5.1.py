# Передается целое число (мб отрицательное) программа возвращает True,
# если из этого числа извлекается квадратный корень без остатка как пример таких чисел
# это (1, 4, 9, 16). Иначе возвращать False.

a = int(input('Введите число: '))
if a < 0:
    a = -a
b = a ** 0.5
c = b - int(b)
if c > 0:
    print('False')
else:
    print('True')

