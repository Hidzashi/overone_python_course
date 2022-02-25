#task_1
text = input('введите предложение ')
symbol = input('введите искомый символ ')
if symbol in text:
    i = 0
    while text[i] != symbol:
        i += 1
    print(i)
else:
    print('такого символа в предложении нет')

#task_2
distance = float(input('введите робег за сегодня '))
y = float(input('введите желаемый пробег '))
now = distance
day = 1
while now < y:
    now += now / 10
    day += 1
print(f'чтобы увеличить побег с {distance} км до {y} км потребуется {day} дней тренировок')

#task_3_var1
num = input('введите ваше любомое число ')
while not num.isdigit():
    num = input('введите ваше любомое число ')
print(f'{num} - прекрасное число')

#task_3_var2
while not (num := input()).isdigit():
    pass