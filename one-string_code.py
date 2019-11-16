print('\n')

# Сложить все числа от одного до 2^25
print(f'{sum(range(1 , 2 ** 25 + 1))} \n')

#Вычислить факториал 1000
import math
print(f'{math.factorial(1000)} \n')

#Удвоить все нечетные числа в списке
l = range(10)
l = [2*i if i % 2 == 1 else 0 for i in l]
print(f'{l} \n')

#Найти элементы списка, отсутствующие в другом
l1 = ['a', 'b', 123, 1.1, ['abc'], (1, 2 ,3)]
l2 = ['b', 1.1, ['abc'], 123]

print(f'[s for s in l1 if s not in l2] \n')

#Считать строчку с клавиатуры и развернуть
s = str(input())
print(s[::-1])
