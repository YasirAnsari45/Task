a =  [1, 3, 5, 7, 9]
c = 0
for i in a:
	if i%3==0 or i%5==0:
		c+=1
print(c)

a = "hello world python".split()
b = a[::-1]
c = ""
for i in b:
	c+=i
	c+=" "
print(c)

a =  "cat".split()
b=  "bat".split()
for i in a:
	if i in b:
		print(True)
		break
else:
	print(False)
	

a = 4
b='*'
for i in range(a):
  print(b)
  b=" "+b 


a =  "madam racecar apple".split()
b = []
for i in a:
	if i==i[::-1]:
		b.append(i)
print(max(b,key=len))














