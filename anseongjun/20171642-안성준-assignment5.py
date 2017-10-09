import time

def refibo(n):
    if n<=1:
        return n
    return refibo(n-1)+refibo(n-2)

def iterfibo(n):
    if n<=1:
        return n
    elif n>=2:
        a=0
        b=1
        c=1
        for i in range(n):
            a=b+c
            c=b
            b=a
        return a

start=time.time()
refibo(int(input("재귀피보나치함수=")))
end=time.time()
print("재귀피보나치함수 시간=",end-start)

start2=time.time()
iterfibo(int(input("반복문피보나치함수=")))
end2=time.time()
print("반복문피보나치함수 시간=",end2-start2)

