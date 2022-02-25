#task_1

text = input('введите строку')
text = text.strip()
space_1 =  text.find(' ')
space_2 =  text.rfind(' ')
last = text[space_2+1:]
first = text[:space_1]
central  text[first:last + 1]
text = last + central + first
print(text)
#text = text.replace(last, '')
#text = text.replace(first, '')
#print(last, text, first)

#task_2

text = input('введите слово').lower().replace(' ','')
#a = int(len(text)/2)
#hvost = text[-1:-a-1:-1]
#golova = text[0:a]
hvost = text[::-1]
#golova = text[0:a]
res = 'palindrom' if text == hvost else 'ne palindrom'
#if hvost == text:
    res = True
#else:
    res = False
print(res)

#task_3

text = input('введите текст ')
# a = (lent(text) // 2) if lent(text) $ 2 == 0 else (lent(text) // 2) +1
# print(text[:a])
# print(text[a:])

if len(text) % 2 == 0:
    a = lent(text) // 2
    print(text[:a])
    print(text[a:])
else:
    a = (lent(text) // 2) + 1
    print(text[:a])
    print(text[a:])


#    #task_4

text = input('введите слово ')
text = text.rstrip()
vowels = 'аоуыэеёиюяeyuioa'
if text[0].lowers() in vowels:
    print('слово начинается на гласную')
else:
    print('слово начинается на согласную')