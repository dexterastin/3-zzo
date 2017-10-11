import time

def refibo(n):
    if n<=1:
        return n
    return refibo(n-1)+refibo(n-2)

def iterfibo(n):
    if n<=2:
        return 1
    elif n>=3:
        sum=0
        f1=1
        f2=1
        for i in range(n-2):
            sum=f1+f2
            f2=f1
            f1=sum
        return sum
n=int(input("enter a number:"))
start=time.time()
refibo(n)
end=time.time()
print(refibo(n),"재귀피보나치함수 시간=",end-start)


start2=time.time()
iterfibo(n)
end2=time.time()
print(iterfibo(n),"반복문피보나치함수 시간=",format(end2-start2, '.18f'))
