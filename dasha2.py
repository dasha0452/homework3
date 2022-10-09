from random import randint
a = []                              # объявили массив а
b = []                              # объявили массив б
ab = []                             # объявили массив пересечений массивов а и б

len_a = int(input("enter len a: ")) # просим пользователя ввести длину а
len_b = int(input("enter len b: ")) # просим пользователя ввести длину б

for ia in range(0,len_a):           # цикл генерации случайных чисел с повторением до длины а
    ia = randint(0,100)
    a.append(ia)

for ib in range(0,len_b):           # цикл генерации случайных чисел с повторением до длины б
    ib = randint(0,100)
    b.append(ib)

for i in a:                         # для каждого элемента массива а проверяем, есть ли такой же в массиве б, если есть - добавляем в пересечение
    if i in b:
        ab.append(i)

print("A:",a)                            # результат
print("Б:",b)
print("A & Б:",ab)
