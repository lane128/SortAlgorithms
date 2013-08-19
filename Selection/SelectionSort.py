US=[13,4,9,5,3,6,1,2,8]
#US = [27, 33, 28, 4, 2, 26, 13, 35, 8, 14]

def SelectionSort(n):
	m=len(n)
	if m<=1:
		return n
	for i in range(m):
		temp=i
		for j in range(i+1,m):
			if n[temp]>n[j]:
				temp=j
		n[i],n[temp]=n[temp],n[i]
		print n
	return n

if __name__ == '__main__':
	x=SelectionSort(US)
	print x
			
				
			

		