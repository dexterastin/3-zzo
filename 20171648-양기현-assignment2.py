while 1:
    n = input("Enter a number: ")

    if not n.isdigit() and n != "-1":
        print("Please enter value correctly.")
        continue

    n = int(n)

    if n == -1:
        break

    factorial = 1

    for value in range(1, n + 1):
        factorial *= value

    print("%d! = %d" % (n, factorial))
