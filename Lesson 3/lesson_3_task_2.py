# Напишите программу, которая проверяет является ли число четным

a = int(input("Введите число: "))
b = a % 2
if b == 0:
    print(f"'{a}' - четное" )
else:
    print(f"'{a}' - нечетное")