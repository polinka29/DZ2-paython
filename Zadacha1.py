# Для натурального n создать словарь индекс-значение, состоящий 
# из элементов последовательности 3n + 1.
# Пример:Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('Введите число: '))
i = 1
for i in range(n + 1):
    a = 3 * i + 1
    i += 1
    print(a, end=' ')