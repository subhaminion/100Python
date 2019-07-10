# def recurring_words(string):
# string = '77150'

# counts = {}
# for digit in string:
# 	if digit in counts:
# 		counts[digit] = counts[digit] + 1
# 	else:
# 		counts[digit] = 1
# print(counts)

# print(recurring_words('77150'))

# d = {x:0 for x in range(10)}

# for digit in string:
# 	digit = int(digit)
# 	d[digit] += 1

# for x in range(10):
# 	print(x, d[x])


# string = input()
# string = str(string)

# numlist = [0] * 10

# for digit in string:
# 	numlist[int(digit)] += 1

# for i in range(10):
# 	print(i, numlist[i])
# open_list = ['(', '[', '{']
# close_list = [')', ']', '}']

# def matched(str):
#     count = 0
#     for i in str:
#         if i in open_list:
#             count += 1
#         elif i in close_list:
#             count -= 1
#         if count < 0:
#             return False
#     return count == 0

# print(matched(''))

