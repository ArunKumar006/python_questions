def fact(n):
    if n<=1:
        return 1
    else:
        return n * fact(n-1)
print(fact(6))


def fact_iter(n):
    s=1
    for i in range(1,n+1):
        s=s*i
        print(s)
    return s
print(fact_iter(4))