US=[4,1,5,3,6,9,2,8]

def bubble(List):
	for j in range(len(List)-1,1,-1):
		print List
		for i in range(0,j):
			if List[i]>List[i+1]:
				List[i],List[i+1]=List[i+1],List[i]
	print List

if __name__ == '__main__':
	bubble(US)
	
