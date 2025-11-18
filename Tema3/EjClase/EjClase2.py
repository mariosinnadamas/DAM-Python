def factorial(n: int):
    if n==0:
        return 1

    result = 1
    for i in range (1,n+1):
        result *= i
    return result

def factorialrecursiva(n: int):
    if n==0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n:int):
    if n <=0:
        return 0
    elif n == 1:
        return 1

    a, b = 0,1

    for i in range (1,n):
        a,b = b, a + b
    return b

def fibonacci_recursivo(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)




print(factorial(5))
print(factorialrecursiva(5))
print(fibonacci(11))
print(fibonacci_recursivo(11))