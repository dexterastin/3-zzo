import time

def fibo(n):
 	if n <= 1:
 		return n
 	else:
 		return fibo(n - 1) + fibo(n - 2)

def iterfibo(n):
    list=[0,1]
    if n<=1:
        return n
    else:
        for i in range(n-1):
            t = list[i] + list[i+1]
            list.append(t)
        return list[-1]

while True:
  nbr = int(input("Enter a number: "))
  if nbr == -1:
     break
  ts = time.time()
  fibonumber = iterfibo(nbr)
  ts = time.time() - ts
  print("IterFibo(%d)=%d, time %.6f" % (nbr, fibonumber, ts))
  ts = time.time()
  fibonumber = fibo(nbr)
  ts = time.time() - ts
  print("Fibo(%d)=%d, time %.6f" % (nbr, fibonumber, t

                                    
 ----------------------------------------------------------------------------------
                                    
                                    import time

def fibo(n):
 	if n <= 1:
 		return n
 	else:
 		return fibo(n - 1) + fibo(n - 2)

def iterfibo(n):
    list=[0,1]
    count =0
    if n<=1:
        return n
    else:
        while (count != n-1):
                t = list[0] + list[1]
                list.append(t)
                del(list[0])
                count = count +1
        return list[-1]

while True:
  nbr = int(input("Enter a number: "))
  if nbr == -1:
     break
  ts = time.time()
  fibonumber = iterfibo(nbr)
  ts = time.time() - ts
  print("IterFibo(%d)=%d, time %.6f" % (nbr, fibonumber, ts))
  ts = time.time()
  fibonumber = fibo(nbr)
  ts = time.time() - ts
  print("Fibo(%d)=%d, time %.6f" % (nbr, fibonumber, ts))
