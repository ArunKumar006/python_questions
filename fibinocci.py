def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))


def fib():
    x,y=0,1
    while True:
        yield x
        x,y=y,x+y

n=10
fib_gen=fib()
for _ in range(n):
    print(fib_gen.__next__())