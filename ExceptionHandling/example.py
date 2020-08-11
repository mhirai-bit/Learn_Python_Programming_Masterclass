def factorial(n):
    if n  < 1:
        return 1
    else:
        return n * factorial(n - 1)

try:
    print(factorial(900))
except (RecursionError, OverflowError):
    print("This program cannot calculate factorials that large")

print("Program terminating")