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
---------------------------------------------------
while (True):
        result = 1
        try:
            n = int(input("Input your number : "))
        except ValueError:
            print("문자열 또는 자연수가 아닌 수가 입력되었습니다. 자연수를 입력해주세요.")
        else:
            if(n==-1):
                    break
            elif (n<-1):
                print("음수가 입력되었습니다. 자연수를 입력해주세요.")
            else:
                    for i in range (1,n+1):
                            result = i * result
                    print(result)
