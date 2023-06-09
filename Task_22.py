# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = int(input('Введите количество элементов 1-го множества: '))
elements_n = set()
for i in range(n):
    elements_n.add(int(input()))
elements_n = [*set(elements_n)]           # заполнение множества
print('Множество:', sorted(elements_n))

m = int(input('Введите количество элементов 2-го множества: '))
elements_m = set()
for i in range(m):
    elements_m.add(int(input()))
elements_m = [*set(elements_m)]
print('Множество:', sorted(elements_m))

u = sorted(list(elements_n and elements_m))       # ищет элементы, которые есть и в множестве 1 и в множестве 2

print(f'Числа, встречающиеся в обоих наборах: {u}')   # если написать sorted(list(elements_n and elemens_m), reverse = True) - по убыванию