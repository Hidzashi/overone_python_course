#task_1

# num = input('введите номер телефона в формате +375********* ')
# num = num.replace(' ', '')
# num = num.replace('-', '')
# kode = '29 25 33 44'
# number = num[4:]
# if num.startswith('+375'):
#     if num[4:6] in kode and number.isdigit() and len(number) == 9:
#         print('Ok')
#     else:
#         print('неверно введен номер')
# else:
#     print('неврно введен код страны')
# print(num)

#task_2

# text_1 = input('введите первую строку ')
# text_2 = input('введите вторую строку ')
# t1 = text_1[1] + text_1[0] + text_1[2:]
# t2 = text_2[1] + text_2[0] + text_2[2:]
# text = t1 + ' ' + t2
# print(text)

#task_3

# text = input('введите строку ')
# first = text[0]
# second = text[1:]
# text_new = first + second.replace(first, '$')
# print(text_new)

#task_4

text = input('введите текст из 4 слов ')
first_space = text.find(' ')
last_space = text.rfind(' ')
word_1 = text[:first_space]
word_4 = text[last_space + 1:]
t = text[first_space +1:last_space]
central_space = t.find(' ')
word_2 = t[:central_space]
word_3 = t[central_space +1:]
l_1 = len(word_1)
l_2 = len(word_2)
l_3 = len(word_3)
l_4 = len(word_4)
if l_2 < l_1 > l_3 and l_1 > l_4:
    print('длиннее первое слово')
elif l_3 < l_2 > l_4:
    print('длиннее второе слово')
elif l_3 > l_4:
    print('длиннее третье слово')
else:
    print('длиннее четвертое слово')
#print(word_1, word_2, word_3, word_4)
