# task_1
#
# text = input('введите предложение ')
# text = text.lower()
# for i in text:
#     if text.count(i) == 1:
#         print(f'уникальные символы: {i}')

# task_2 переделать!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# num = input('введите число ')
# num_int = int(num)
# k = 0
# for i in range(2, num_int + 1, 2):
# 	k += 1
# 	text += i + ' '
# 	if k % 5 == 0:
# 		text += '\n'
# print(text)

# task_3 доработать!!!!!!!!!

# word_1 = input('введите первое слово ')
# word_2 = input('введите второе слово ')
# word_1 = word_1.lower()
# word_2 = word_2.lower()
# k = 0
# if word_1.isalpha() and word_2.isalpha():
# 	if len(word_1) == len(word_2):
# 		for i in range(len(word_1)):
# 			if word_1.count(word_1[i]) == word_2.count(word_1[i]):
# 				k +=1
# 				if k == len(word_1):
# 					print('ok')
# 			else:
# 				print('no')
# 	else:
# 		print('no')
# else:
# 	print('неверно введены слова')

# task_4

text = input('введите предложение ')
n = 0
for i in range(len(text) - 1):
	if text[i] == text[i+1]:
		n += 1
print(f'{n=}')



