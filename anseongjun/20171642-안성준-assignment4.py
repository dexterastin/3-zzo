def fac(n):
    num = 1
    if n == 1:
        return 1
    else:
        for i in range(1, n+1):
            num *= i
        return num

def C(n,m):
    try:
        a = fac(n) / (fac(m) * fac(n-m))
        return a
    except:
        print("Error")

def reculC(n,m):
    if n == m or m == 0:
        return 1
    else:
        return reculC(n-1,m) + reculC(n-1,m-1)

n = int(input("n ="))
m = int(input("m ="))

print("C(n,m) = " ,C(n,m))
print("reculC(n,m) = ", reculC(n,m))