def combination_factorial(n, r):
    if r == 0:
        return 1
    elif n < r:
        return 0
    else:
        return factorial(n) / (factorial(r) * factorial(n - r))


def combination_recursive(n, r):
    if r == 0:
        return 1
    elif n < r:
        return 0
    else:
        return combination_recursive(n - 1, r - 1) + combination_recursive(n - 1, r)


def factorial(n):
    if n == 2 or n == 1:
        return n
    else:
        return n * factorial(n - 1)
    pass


while True:

    try:
        n = int(input("Enter n: "))

        if n == -1:
            break

        r = int(input("Enter m: "))
        
        if n < 0 or m < 0:
            print("양수를 입력해주세요")
            continue

    except ValueError:
        print("Enter correct value.")

    print("Cf(%d, %d) = %d" % (n, r, combination_factorial(n, r)))
    print("C(%d, %d) = %d" % (n, r, combination_recursive(n, r)))
