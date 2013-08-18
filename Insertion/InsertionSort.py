US=[13,4,9,5,3,6,1,2,8]
#US = [27, 33, 28, 4, 2, 26, 13, 35, 8, 14]


#This is the recursion solution,but not represent the basic procedure of InsertionSort.
def insertionSort_recursion(n):
	if len(n) == 1:
		return n
	b = insertionSort_recursion(n[1:])
	m = len(b)
	print b
	for i in range(m):
		if n[0] <= b[i]:
			return b[:i]+[n[0]]+b[i:]
	return b + [n[0]]


def  insertionSort(n):
	if len(n)==1:
		return n
	m=len(n)
	for i in range(1,m):
		temp=n[i]
		for j in range(i-1,-1,-1):
			if n[j]>temp:
				n[j+1]=n[j]
				if j==0:
					n[j]=temp
					break
			else:
				n[j+1]=temp
				break	
		print n
	return n


if __name__ == '__main__':
	print US
	insertionSort(US)
	