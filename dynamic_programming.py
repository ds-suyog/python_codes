

list_num = [0,1]
print(list_num)
n = 6
for i in range(2,n,1):
	print(i)
	list_num.append(list_num[i-1] + list_num[i-2])

print(list_num)
