n=int(input("n="))
m=int(input("m="))
devided=1
deviding1=1
deviding2=1
for i in range(n):
        devided*=i+1
for j in range(m):
        deviding1*=j+1
for k in range(n-m):
        deviding2*=k+1
RegC=devided/(deviding1*deviding2)
print("Factorial로 계산한 결과: ", RegC)
def Recursive(n, m):
        if m==0 or m==n:
                return 1
        return Recursive(n-1, m)+Recursive(n-1, m-1)
print("재귀함수로 계산한 결과: ", Recursive(n, m))
