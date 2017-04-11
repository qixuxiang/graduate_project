lst1=[1,0,1,0,1,0,1,1]
lst=[]
for i in range(6):
	lst.append([])

lst[1]=[1,1,1,1,1,0,1,1]
lst[2]=[1,1,1,0,1,1,1,1]
lst[3]=[1,0,0,0,0,0,0,1]
lst[4]=[1,0,1,0,1,0,0,1]
lst[5]=[1,0,1,0,1,0,1,1]
print(lst)
	
if __name__ == '__main__':
	arr=[]
	for l in lst[1:6]:
		if len(lst1)!=len(l):
			print(len(lst1))
			print(len(l))
			print("wrong!!")
		amount=0
		for i in range(len(lst1)):
			if l[i]^lst1[i]:#亦或越小，相似度越高
				amount+=1
		arr.append(amount)
		v=min(arr)
	print(arr)
	print(arr.index(v)+1)


