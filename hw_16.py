#task_1
# with open("input.txt", "r", encoding = "utf-8") as file, open("output_1.txt", "w", encoding = "utf-8") as file_2:
#     lst = [line.strip() for line in file]
#     s = 0
#     for i in lst:
#         if i.isdigit():
#             s += int(i)
#     file_2.write(f'сумма чисел из строки - {lst} равна {s}')

#task_2
# with open("input_1.txt", "r", encoding = "utf-8") as file, open("output_2.txt", "w", encoding = "utf-8") as file_2:
#     lst = [line.strip().split() for line in file]
#     text = ''
#     for _ in lst:
#         text += ' '.join(_) + '\n'
#     vowels = 'иуеэоаыяюё'
#     counter_v = 0
#     counter_o = 0
#     for i in lst:
#         for j in i:
#             if j[0].isalpha() and j[0].lower() in vowels:
#                 counter_v += 1
#             elif j[0].isalpha() and j[0].lower() not in vowels:
#                 counter_o += 1
#     file_2.write(text)
#     file_2.write(f'слов на гласную больше' if counter_v>counter_o else 'слов, на согласную больше\n')
#     file_2.write(f'на гласную - {counter_v}, на согласную - {counter_o}')

# task_3
#
# data = {
#     1: 'partiya_a',
#     2: 'partiya_b',
#     3: 'partiya_c',
#     4: 'partiya_d',
#     5: 'partiya_e',
# }
# data_1 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
# with open("input_3.txt", "r", encoding = "utf-8") as file, open("output_3.txt", "w", encoding = "utf-8") as file_2:
#     lst = [line.strip().split() for line in file]
#     for key in data.keys():
#         for i, j in enumerate(lst[0]):
#             if j.isdigit() and key == int(j):
#                 data_1[key] += 1
#                 lst[0][i] = ' '
#     counter = 0
#     for t in lst[0]:
#         if t != ' ':
#             counter += 1
#     for i in data_1:
#         file_2.write(f'за {data[i]} - {data_1[i]}\n')
#     file_2.write(f'испоченных бланков - {counter}')

#task_4
# with open("input_1.txt", "r", encoding = "utf-8") as file, open("output_4.txt", "w", encoding = "utf-8") as file_2:
#     lst = [line.strip().split() for line in file]
#     for i in range(len(lst)):
#         counter = 0
#         for j in range(len(lst[i])):
#             counter += len(lst[i][j].replace(',', '').replace('.', ''))
#         file_2.write(f'в {i+1} строке {len(lst[i])} слов и {counter} букв\n')