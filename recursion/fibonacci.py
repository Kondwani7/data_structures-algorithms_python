def fibonacci(n):
    if (n < 0):
        return (f"Input number should be equal to or above 0:{n}")
    elif n == 0:
        return 0
    elif (n == 1 or n == 2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))