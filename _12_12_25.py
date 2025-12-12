g"""a = 123 
b = 321
sum1 = 0
sum2 = 0
while a>0:
	c = a%10
	sum1+=c
	a = a//10
while b>0:
	d = b%10
	sum2+=d
	b = b//10
result = sum1== sum2
print(result)"""

"""a = 9875
sum1 = 0
while a>0:
	c = a%10
	sum1+=c
	a = a//10
	if  sum1> 9 and  a==0:
		a = sum1
		sum1 = 0
print(sum1)"""


"""list1 =  [1, 5, 3]
list2 = [0, 5, 2]
count = 0
for i in range(len(list1)):
	if list1[i]>list2[i]:
		count+=1
print(count)"""

a = "abcaad"
character = 'a'
s = ""
l = []
count=0
for i in a:
	if i==character:
		l.append(count)
		count=1
	else:
		s+=i
		count+=1
l.remove(0)
print(min(l))
		
















