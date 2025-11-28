a = "I love Python".split(" ")
b =  "Python is awesome".split(" ")
list1 = []
for i in a:
	if i in b:
		list1.append(i)
print(list1)


a =  [1, 2, 3, 4, 6]
K = 6
for i in range(len(a)):
 for j in range(i+1,len(a)+1):
    if i*j == K:
    
     print((i,j))

 a =  "hello".lower()
vowel = "aeiou"
l = []
s = ""
for i in a:
	if i in vowel:
		l.append(i)
for j in a: 
	if j in vowel:
		s+=l[-1]
		l.pop()
	else:
		s+=j
print(s)



a = ["flower", "flow", "flight"]
a.sort()
s = ""
for i in range(len(a[0])):
	if a[0][i] == a[-1][i]:
		s+=(a[0][i])
	else:
		break
print(s)







