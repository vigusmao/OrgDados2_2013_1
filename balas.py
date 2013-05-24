def f(n, m):
    b = n - m*(m+1)/2
    if b < 0:
        return 0
    if b == 0:
        return 1

    return g(b, m)


memo = {}

def g(n, m):

    if (n,m) in memo:
        return memo[(n,m)]

        
    if n < 0:
        return 0

    if m == 1:
        return 1

    r = g(n, m-1) + g(n - m, m)

    memo[(n,m)] = r
    return r
