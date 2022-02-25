# task_1
num = input('введите семизначное число ')
odd = 0
even = 0
for i in range(0, len(num)):
	if int(num[i]) % 2:
		odd +=1
	else:
		even += 1
if odd > even:
		print(int(num[0]) * int(num[2]) * int(num[4]))
else:
		res = 0
		for i in range(0, len(num)):
			res += int(num[i])
		print(res)

# task_2
text = input('введите предложение ')
vowels = 'аоуыэяёеиюeyuioa'
text = text.lower()
vow = 0
con = 0
res_vow = ''
for i in range(0, len(text)):
		if text[i].isalpha() == False:
			continue
		elif text[i] not in vowels:
			con +=1
		elif text[i] in vowels:
			res_vow += text[i]
			vow +=1
if vow == con:
	print(res_vow)
else:
	print('гласных - ', vow, 'согласых - ', con)

# task_3
import random
numbers = 0
rnumbers = 0
four_i = []
for i in range(7):
	num_1 = int(input('первое число - '))
	num_2 = int(input('второе число - '))
	print(rnum_1 := random.randint(1, 20))
	print(rnum_2 := random.randint(1, 20))
	if num_1 > rnum_1:
		numbers += 1
	elif num_1 < rnum_1:
		rnumbers += 1
	if num_2 > rnum_2:
		numbers += 1
	elif num_2 < rnum_2:
		rnumbers += 1
	if i == 3:
		four_i.append(rnum_1)
		four_i.append(rnum_2)
if numbers != rnumbers:
	print(f'введенные числа оказались больше рандомных {numbers} раз')
else:
	print(four_i)

#task_4

import random

num = int(input('количество чисел '))
n = input('проверяемая цифра ')
numbers = [a := str(random.randint(1,50)) for _ in range(num)]
numbers = ' '.join(numbers)
print(numbers)
print(f'цифра {n} встречается в заданных числах {numbers.count(n)} раз(а)')

#task_5

text = input('введите предложение ')
text += ' '
res = []
num = ''
i = 0
while i < len(text)-2:
		if text[i].isdigit():
			while text[i].isdigit():
				num = num + str(text[i])
				i += 1
			res.append(int(num))
			num = ''
		else:
			i += 1
for i in res:
	print(i)

#task_6

text = input('введите слово ')
vowels = 'аоуыэяёеиюeyuioa'
up = 0
down = 0
vow = 0
if text.isalpha() == False:
	print('не верно введено слово ')
else:
	text_1 = text + ' '
	for i in range(len(text)):
		if text_1[i].isupper() and text_1[i+1].isupper():
			up += 1
		elif text_1[i].islower() and text_1[i+1].islower():
			down +=1
		if text_1[i].lower() in vowels:
			vow += 1
	print(f'{up} - пар(а) верхнего, {down} - пар(а) нижнего,\
	всего букв - {len(text)}, гласных - {vow}, согласных - {len(text)-vow} ')