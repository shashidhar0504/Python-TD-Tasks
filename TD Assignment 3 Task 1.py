#Task 1: Calculate Factorial Using a Function

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

n = 1
result = factorial(n)
print("Factorial of", n, "is", result)

