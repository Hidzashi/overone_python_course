#task_1
lst_1 = [1, 2, 3, 4, 5, 6, 7]
lst_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
data = {}
for i in range(len(lst_1)):
    data[lst_1[i]] = lst_2[i]
print(data)

#task_2
data = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}
num = int(input('введите натуральное число '))
num = str(num)
res = ''
for i in num:
    res += data[int(i)]
print(res)

#task_3
morze = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
    'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-',
    'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}
text = input('введите сообщение ').lower()
res = ''
for i in text:
    if i != ' ' and (i.isalpha() or i.isdigit()):
        res += morze[i]
print(res)

#task_3+4
morze = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
    'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-',
    'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}
text = input('введите сообщение ').lower()
res = ''
for i in text:
    if morze.get(i) != None:
        res += morze[i]
        res += ' '
print(res)

#task_5
text_1 = input('введите текст ').lower()
text = text_1.split(' ')
print(text)
data = {}
res = {}
for i in text:
    if i not in data:
        data[i] = 1
    else:
        a = data[i]
        del data[i]
        data[i] = a + 1
#print(data)
a = 1
while res == {}:
    for key, val in data.items():
        if data[key] == a:
            res[key] = val
    if res == {}:
        a += 1
#print('res', res)
res_1 = []
for key in res.keys():
    res_1.append(key)
res_1.sort()
print(res_1[0])




