while 1:
    n = int(input("Enter a number: "))

    if not str(n).isdigit():
        print("Please enter value correctly.")
        continue

    if n == -1:
        break

    factorial = 1

    for value in range(1, n + 1):
        factorial *= value

    print("%d! = %d" % (n, factorial))
