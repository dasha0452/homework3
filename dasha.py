from random import randint
m = [] # объявили массив
len = int(input('enter len: ')) # просим пользователя ввести длину массива
for i in range(0, len):  # цикл генерации случайных чисел с повторением до длины, которую ввел пользователь
    i = randint(0, 10000) / 10
    m.append(i)
maximum = m.index(max(m))  # узнаём индекс максимального элемента из массива
for x in m:
    if m.index(x) > maximum:
        m[m.index(x)] = 0 # если индекс элемента в массиве больше максимального то зануляем его
print(m) #результат