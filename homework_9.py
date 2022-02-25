# n = 5
# s_1 = ''
# s_2 = ''
# s_3 = ''
# s_4 = ''
# s_5 = ''
# k = 0
# for i in range(1, n**2+1):
#     while i <= n:
#         s_1 += str(i)
#         break
#     else:
#         if i == n + 1:
#             s_2 += str(i)
#             s_3 += str(i + 1)
#             s_4 += str(i + 2)
#             s_5 += str(i + 3)
#             n -=1
#             i += n
#         else:
#             for _ in range(n):
#                 s_5 = str(i) + s_5
#
#
#     #while i
#
# print(s_1, s_2, s_3, s_4, s_5, i, n, end = '\n')





#for j in range(6, 10):
#	print(j, end = '\n')

	# if j < 6:
	# 	for k in range(16, 20):
	# 		print(k, end = ' ')
	# elif j < 7:
	# 	print('15 24 25 20', end =' ')
	# elif j < 8:
	# 	print('14 23 22 21', end = ' ')
	# elif j < 9:
	# 	for t in range(13, 9, -1):
	# 		print(t, end = ' ')
	#

num = int(input('сколько заплатить ведьмаку?? '))
s = 0
while num > 25:
	num -= 25
	s += 1
while num > 10:
	num -= 10
	s += 1
while num > 5:
	num -= 5
	s += 1
while num >= 1:
	num -= 1
	s += 1
print(s)
