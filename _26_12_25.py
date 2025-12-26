"""lst = [1, 2, 3, 4]
r = []
for i in range(len(lst)):
	mul = 1
	for j in range(i,len(lst)):
		if i==j:
			continue
		else:
			mul*=lst[j]
	r.append(mul)
print(r)"""

"""dict1= {
"Alice": 70000,
"Bob": 80000,
"Charlie": 120000,
"David": 60000,
"Eve": 110000
}
l = []
s = sorted(dict1,key=dict1.get,reverse =True)
for i in s:
	if len(l) != 3:
		l.append((i,dict1[i]))
print(l)"""

"""from collections import Counter
attendance = {
"Monday": ["Ahmed", "Fatima", "Hassan"],
"Tuesday": ["Fatima", "Ali", "Zainab"],
"Wednesday": ["Ahmed", "Hassan", "Ayesha"],
"Thursday": ["Fatima", "Ali", "Hassan"],
"Friday": ["Ahmed", "Fatima", "Zainab", "Ayesha"]
}
l = []
for i in attendance:
	l.extend(attendance[i])
r = Counter(l)
s = sorted(r,key=r.get,reverse=True)
for i in s:
	print(i,r[i])
	break"""

"""lst = [3, 4, -1, 1]
r = []
for i in lst:
	if i>=0:
		r.append(i)
for j in range(min(r),max(r)+2):
	if j not in r:
		print(j)
		break"""

students = [
{"name": "Ahmed", "marks": [85, 90, 78]},
{"name": "Fatima", "marks": [92, 88, 95]},
{"name": "Hassan", "marks": [65, 70, 68]},
{"name": "Ayesha", "marks": [88, 85, 90]}
]
avg = []
def avrg(mark):
	for i in mark:
		print(append((sum(i["marks"])/len(i["marks"])))

avrg(students)








