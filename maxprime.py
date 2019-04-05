def prime(n):
	multarr=[]
	for i in range(1,n+1):
		if n%i==0:
			multarr.append(i)
					
	if len(multarr)==2:
		return True
	else:
		return False
		
def primetest(n):
	multarr=[]
	for i in range(1,n+1):
		if n%i==0 and prime(i):
			multarr.append(i)
	return max(multarr)
	#counter = n
	#while counter > 0:
		#if prime(counter):
			#return counter
			#break;
		#counter -=1
		


n = int(input())
print(primetest(n))