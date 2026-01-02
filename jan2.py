"""lst = [3, 1, 2, 4, 7, 6]
even = []
odd = []
result = []
for i in lst:
	if i%2==0:
		even.append(i)
	else:
		odd.append(i)
result.extend(odd)
result.extend(even)
print(result)"""

"""lst = [16, 17, 4, 3, 5, 2]
result = []
for i in range(len(lst)):
	for j  in range(i+1,len(lst)):
		if lst[i]<lst[j]:
			break
	else:
		result.append(lst[i])
print(result)"""

"""lst = [2, 4, 2]
l = len(lst)//2
if sum(lst[:l])==sum(lst[l+1:]):
	print(l)"""




"""lst = [-1, -2, 3, 4, 5]
pos= []
neg= []
result = []
for i in lst:
	if i>0:
		pos.append(i)
	else:
		neg.append(i)
while pos and neg:
	result.append(neg.pop(0))
	result.append(pos.pop(0))
print(result)"""

lst = [1, 1, 1, 1]
l= len(lst)//2
add = sum(lst[:l])
print(add)




