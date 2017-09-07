while (True):
	result = 1
	print("Input your number")
	n = int(input())
	if(n==-1):
		break
	else:
		for i in range (1,n+1):
			result = i * result
		print(result)
