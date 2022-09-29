# Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
# Пример:- Для n = 5: сумма = 11,55

num = int(input('Введите число: '))
a = [round((1 + 1 / x) ** x) for x in range(1, num + 1)]
sum = 0
for i in a:
    sum = sum + i
print(f'{a} sum = {sum}')