#task_1

#a = input('введите первое число ')
#b = input('введите второе число ')
#c = input('введите третье число ')
#a = int(a)
#b = int(b)
#c = int(c)
#srednee  = (a + b + c)/3
#srednee = round(srednee, 2)
#print('среднее арифметическое трех чисел равно ', srednee)

#task_2

#kat_1 = input('введите длину первого катета прямоугольного треугольника ')
#kat_2 = input('введите длину второго катета прямоугольного треугольника ')
#kat_1 = int(kat_1)
#kat_2 = int(kat_2)
#gip = (kat_1**2 + kat_2**2)**0.5
#gip = round(gip, 2)
#print('гипотенуза прямоугольного треугольника равна ', gip)

#task_3

#ch = input('введите трехзначное число ')
#ch = int(ch)
#hun = int(ch*0.01)
#print('первая цифра числа - ', hun)
#tens = int((ch-hun*100)*0.1)
#print('вторая цифра числа - ', tens)
#units = int((ch-hun*100-tens*10))
#print('третья цифра числа - ', units)
#sum = hun + tens + units
#print('сумма цифр числа - ', sum)

#task_4

#a = input('введите возраст отца ')
#b = input('введите возраст сына ')
#a = int(a)
#b = int(b)
#r = abs(a - b * 2)
#print(r, 'лет (года)')
a = input('введите возраст отца ')
b = input('введите возраст сына ')
a = int(a)
b = int(b)
r = (a - b * 2)
if r == 0:
 	print('сейчас отец в два раза старше сына ')
elif r > 0:
	print('через ', r, ' лет ')
else:
	print(r*(-1), 'лет назад')

