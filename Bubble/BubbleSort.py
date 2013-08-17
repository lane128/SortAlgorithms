UnSortedList=[4,1,5,3,6,9,2,8]

def bubble(List):
	for j in range(len(List)-1,1,-1):
		for i in range(0,j):
			if List[i]>List[i+1]:
				List[i],List[i+1]=List[i+1],List[i]
	return List

if __name__ == '__main__':
	print 'the original list is {0} '.format(UnSortedList)
	x=bubble(UnSortedList)
	print 'the sorted list is {0}'.format(x)
