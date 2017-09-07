n=0
factorial=1
while n!=-1:
    n = int(input("enter a number:"))
    for i in range(n):
        j=i+1
        factorial *= j

    if n==-1:
        break

    if n<-1:
        print("양의 정수가 아님")
        continue

    print("%d!=%d"%(n,factorial))
    factorial=1