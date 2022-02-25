# import random
# res = []
#
# for j in range(9):
#     str = []
#     i = 0
#     while i < 9:
#         if (a := random.randint(1,9)) not in str:
#             str.append(a)
#             i += 1
#         else:
#             pass
#     if j == 1:
#         res.append(str)
#     elif j > 1:
#         p = 0
#         for k in res:
#             for b in range(0, 9):
#                 if k[b] != str[b]:
#                     p += 1
#                     if p == 9:
#                         res.append(str)
#                 else:
#                     j -= 1
#                 #break
#             #break
#
#     #i = 0
# for i in res:
#     print(i)
# # while t < 8:
# #     while j < 9:
# #         if (a := random.randint(1, 9)) not in str_1:
# #             str_1.append(a)
# #             j += 1
# #         else:
# #             pass
# #     for b in res:
# #         l = 0
# #         for p in range(0,9):
# #             if b[p] != str_1[b]:
# #                 l += 1
# #             else:
# #                 break
# #         if l == 9:
# #             res.append(str_1)
# #             t += 1
# # print(res)

import random

j = 0
res = []
charters = 9

while j < charters:
    i = 0
    str = []
    genNew = 0

    while i < charters:
        if (a := random.randint(1, 9)) not in str:
            str.append(a)
            i += 1

    res.append(str)

    if j > 0:
        for h in range(charters):
            for v in range(j):
                if res[j][h] == res[v][h]:
                    genNew = 1

        if genNew == 1:
            res.remove(str)
            j -= 1

    j += 1  # while j < charters

for i in res:
    print(i)







