def fibo(i):
	fibo_seq=[1,2]
	value = 0
	for n in range(i+1):
		if n == 0:
			value = fibo_seq[0]
		elif n== 1:
			value = fibo_seq[1]
		else:
			fibo_seq.append(fibo_seq[n-1] + fibo_seq[n-2])
	if n < 2:
		return value
	else:
		return fibo_seq[n-1]

def fibosum(n):
	i=0
	fiboarr=[1,2]
	evenarr=[]
	sum=0
	while fiboarr[i-1] < n:
		if i > 1:
			fiboarr.append(fibo(i+1))
		i+=1
	for i in range (len(fiboarr)):
		if fiboarr[i]%2==0 and fiboarr[i]<n:
			evenarr.append(fiboarr[i])
	return evenarr
	

n = int(input())
print(fibosum(n))