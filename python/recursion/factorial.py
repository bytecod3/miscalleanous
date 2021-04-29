def factorial_recursive(n):
    # base case: 1! = 1
    if n == 1:
        return 1

    # recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)


if __name__ == '__main__':
    print(factorial_recursive(7))