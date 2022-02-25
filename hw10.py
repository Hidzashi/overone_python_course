#task_1
import random

numbers = [random.randint(0, 15) for i in range(int(input('количество чсел в списке ')))]
n = int(input('на сколько позиций сместить элементы? '))
num = []
if n >= 0:
    while n > len(numbers):
        n -= len(numbers)
    for i in range(-n, len(numbers) - n):
        num.append(numbers[i])
    print(numbers, num, end='\v')
elif n < 0:
    while abs(n) > len(numbers):
        n += len(numbers)
    for i in range(-n-1, -len(numbers) - n - 1, -1):
        num.insert(0, numbers[i])
    print(numbers, num, end='\v')

#task_2
lst = [23, 7, '-', [1, 4, 'f'], 'iuy', 'op']
i = 0
while i < len(lst):
    if isinstance(lst[i], str):
        i +=1
    else:
        del lst[i]
print(lst)

#task_3

numbers = [random.randint(0, 15) for i in range(int(input('количество чсел в списке ')))]
print(numbers)
for i in range(len(numbers)//2):
    numbers[i],numbers[-i-1] = numbers[-i-1],numbers[i]
print(numbers)




