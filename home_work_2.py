# task_1

num_1 = int(input('введите первое число '))
num_2 = int(input('введите второе число '))
if abs(num_1 - num_2) == 135:
    print('yes')
else:
    print('No')

# task_2

num = float(input('введите число '))
if abs(num) <= 100:
    print(' + ')
else:
    print(' - ')

# task_3

num = int(input('введите номер месяца (от 1 до 12) '))
if 2 < num < 6:
    print('весна')
elif 5 < num < 9:
    print('лето')
elif 8 < num < 12:
    print('осень')
elif num == 12 or num == 1 or num == 2:
    print('зима')
else:
    print('не верно введен номер месяца')

#task_4

num_1 = float(input('введите первое число '))
num_2 = float(input('введите второе число '))
num_3 = float(input('введите третье число '))
if num_1 > 10 and num_2 > 10 and num_3 > 10:
    print('yes')
else:
    print('no')

# task_5

num_1 = float(input('введите первое число '))
num_2 = float(input('введите второе число '))
num_3 = float(input('введите третье число '))

if num_1 == 0:
    num_1 = 1
if num_2 == 0:
    num_2 = 1
if num_3 == 0:
    num_3 = 1

if num_1 < 0 and num_2 * num_3 < 0 or num_1 * num_2 < 0 and num_3 < 0:
    print(' 2 negative')
elif num_1 > 0 and num_2 * num_3 < 0 or num_1 * num_2 < 0 and num_3 > 0:
    print(' 1 negative')
elif num_1 < 0 and num_2 < 0 and num_3 < 0:
    print(' 3 negative')
else:
    print('no negative')

# task_5*

num_1 = float(input('введите первое число '))
num_2 = float(input('введите второе число '))
num_3 = float(input('введите третье число '))
k = 0
if num_1 < 0:
    k = k + 1
if num_2 < 0:
    k = k + 1
if num_3 < 0:
    k = k + 1
print(k, ' negative numbers')

# task_5**

num_1 = float(input('введите первое число '))
num_2 = float(input('введите второе число '))
num_3 = float(input('введите третье число '))
print((num_1 < 0) + (num_2 < 0) + (num_3 < 0))

