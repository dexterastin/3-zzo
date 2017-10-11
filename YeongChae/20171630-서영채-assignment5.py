import time

def fibo(n):
	if n <= 1:
		return n
	else:	
		return fibo(n - 1) + fibo(n - 2)

def iterative(n):
	list=[0,1]
	newbie=0
	if n<=1:
		return n
	else:
		for i in range(n-1):
			newbie=list[i]+list[i+1]
			list.append(newbie)
		return list[-1]
	 	


while True:
	nbr = int(input("Enter a number: "))
	if nbr == -1:
		break
	ts = time.time()
	fibonumber1 = fibo(nbr)
	ts = time.time() - ts
	print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber1, ts))
	ts = time.time()
	fibonumber2 = iterative(nbr)
	ts = time.time() - ts
	print("iterative(%d)=%d, time %.6f" %(nbr, fibonumber2, ts))

