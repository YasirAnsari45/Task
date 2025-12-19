"""String = "leetcode"
Dict = ["leet", "code", "leetcode"]
if String in Dict:
	print(True)
else:
	print(False)"""

"""a =  "abcabcbb"  
s = ""
l = []
for i in a:
	if i not in s:
		s+=i
	else:
		l.append(len(s))
		s=i
print(max(l))"""

a = "hello,,,world,,python,"
l = []
s = ""
r = ""
l1 = []
for i in a:
	if i != ",":
		s+=i
	else:
		l.append(s)
		s=""
for j in l:
	if j != "":
		l1.append(j)
print(",".join(l1)) 


"""a = "3[a]"
a+="1"
count = 0
s = ""
r =""
for i in a:
	if i.isdigit():
		r+=s*int(count)
		count = i
	elif i.isalpha():
		s+=i
print(r)"""

		




	
			
	