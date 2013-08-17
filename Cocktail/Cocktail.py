US=[13,4,9,5,3,6,1,2,8]
#US = [27, 33, 28, 4, 2, 26, 13, 35, 8, 14]

def Cocktail(l_head,l_end):
	for i in range(l_head,l_end,1):
		if US[i]>US[i+1]:
			US[i],US[i+1]=US[i+1],US[i]
			print US
	l_end=l_end-1
	for j in range(l_end,l_head,-1):
		if US[j]<US[j-1]:
			US[j],US[j-1]=US[j-1],US[j]
			print US
	l_head=l_head+1

	if l_head<l_end:
		Cocktail(l_head,l_end)

if __name__ == '__main__':
	print US
	Cocktail(0,len(US)-1)
	print US
	
