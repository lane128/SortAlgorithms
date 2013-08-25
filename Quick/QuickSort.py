US=[13,4,9,5,3,6,1,2,8]
#US = [27, 33, 28, 4, 2, 26, 13, 35, 8, 14]

def QuickSort(n):
	if len(n)<=1:
		return n
	pivot=n[0]
	less=[]
	greater=[]
	for i in range(1,len(n)):
		if n[i]>pivot:
			greater.append(n[i])
		else:
			less.append(n[i])
	return QuickSort(less)+[pivot]+QuickSort(greater)

if __name__ == '__main__':
	x=QuickSort(US)
	print x