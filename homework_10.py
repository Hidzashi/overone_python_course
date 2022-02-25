#task_1

#num = 2457546
#i = 0
#lst = []
#while i < 7:
#	a = num % 10
#	num = num // 10
#	lst.insert(0, a)
#	i +=1
#print(lst)

#task_2

#s = input('введите предложение ')
#lst = s.split(' ')
#lst_1 = []
#for i in lst:
#	if len(i) > 5:
#		lst_1.append(i)
#print(lst_1)

#task_3
#numbers = '2 12'
#num = []
#n = []
#for i in numbers.split(' '):
#	num.append(int(i))
#for i in range(num[0], num[1] + 1):
#	n.append(i)
#print(n)

#task_1+

# import random
# lst = [random.randint(-100, 100) for i in range(int(input('введите количество чисел '))) ]
# print(lst)
# odd_num = []
# even_num = []
# for i in lst:
# 	odd_num.append(i) if i % 2 else even_num.append(i)
# print(f'нечетные: {odd_num},\nчетные: {even_num}')

#task_2+