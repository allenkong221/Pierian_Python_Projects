def numorder(n):
	first=False
	second=False
	third=False
	for i in range(len(n)):
		if n[i]==0:
			first=True
			for j in range(i+1,len(n)):
				if n[j]==7:
					break
				elif n[j]==0:
					second=True
					for k in range(j+1,len(n)):
						if n[k]==0:
							break
						elif n[k]==7:
							third=True
							break
					break
	
	return first and second and third
	
print(numorder([1,4,7,0,6,7,6,0,8,4,7]))