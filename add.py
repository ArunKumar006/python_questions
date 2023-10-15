def add(x,y):
    while y!=0:

        t=x&y
        x=x|y
        y=t<<1

    return x

print(add(6,8))