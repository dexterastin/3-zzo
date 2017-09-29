result=1
num=int(input('Please enter the number: '))
while num>=0:
	if num > 0:
		result=1
		for i in range(1, num+1):
			result=result*i
		print('%d! = ' %num, result)
		num=int(input('Please enter the number again: '))
	elif num == 0:
		print("0! = 1")
		num=int(input('Please enter the number again: '))
	else:
		print("프로그램을 종료합니다. 음수는 계산할 수 없습니다.")
