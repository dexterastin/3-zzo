while 1:
    n = int(input("Enter a number: "))

    if n == -1:
        break
        pass

    if not str(n).isdigit():
        print("Is not amniotic fluid")
        continue
        pass

    factorial = 1

    for value in range(1, n + 1):
        factorial *= value
        pass

    print("%d! = %d" % (n, factorial))
    pass
