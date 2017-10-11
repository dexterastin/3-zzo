import time


def iterfibo(nbr):
    list = [0, 1]

    for idx in range(1, nbr):
        list.append(list[idx - 1] + list[idx])
    return list.pop()


def fibo(nbr):
    if nbr < 2: return nbr
    return fibo(nbr - 2) + fibo(nbr - 1)


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
