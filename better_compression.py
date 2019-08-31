from itertools import groupby

st = 'a12b3c1a1b1'

def split_text(s):
	for k, g in groupby(s, str.isalpha):
		yield ''.join(g)

lol = list(split_text(st))
print(lol)


temp = []
for i in lol:
	if i in temp and not i.isdigit():
		temp[temp.index(i) + 1] = int(temp[temp.index(i) + 1]) + 1
		del(lol[temp.index(i)+1])
	else:
		temp.append(i)

print(''.join(map(str, temp)))