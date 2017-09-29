while 1:
    n = input("Enter a number: ")

    if not n.isdigit() and n != "-1":
        print("Please enter value correctly.")
        continue
        pass

    n = int(n)

    if n == -1:
        break
        pass

    factorial = 1

    for value in range(1, n + 1):
        factorial *= value
        pass

    print("%d! = %d" % (n, factorial))
