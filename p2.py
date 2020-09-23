# https://projecteuler.net/problem=2

def fib(N):

    l = [1,2]
    
    while l[-1] < N:
        n = l[-1] + l[-2]
        l.append(n)

    return l

fib(5)
fib(10)
fib(4000000)

def res(N):
    r = 0
    l = fib(N)
    for n in l:
        if n<N and n%2==0:
            r+=n

    return r

print(res(10))
print(res(4000000)) #4613732

