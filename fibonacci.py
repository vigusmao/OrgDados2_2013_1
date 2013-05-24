def fib(n):

    if n in memo:
        return memo[n]
    
    if n <= 1:
        return 1

    r = fib(n-1) + fib(n-2)
    memo[n] = r
    return r




def fib2(n):
    a, b = 1, 1
    i = 1
    while i < n:
        a, b = b, a+b
        i += 1
    return b



memo = {}

def fib2(n):

    if n in memo:
        return memo[n]
    
    a, b = 1, 1
    i = 1
    while i < n:
        a, b = b, a+b
        i += 1

    memo[n] = b
    return b

