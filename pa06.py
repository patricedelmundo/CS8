def funa(i, j, k):
    sum = 0
    for n in range(i, j+1):
        sum = sum + n**k
    return (sum)

def funb(i, j, k):
    sum = 0
    for n in range(i, j+1):
        sum = sum + n**(-k)
    print(sum)

def func(i, x):
    sum = 0
    for n in range (1, i+1):
        sum = sum + n**x
    return sum

def fund(x):
    return(x**2)

def gmean(x):
    n = len(x)
    sum = 0
    for i in range(n):
        sum = sum + x[i]
    return(sum/n)

def g2(x, n):
    m = len(x)
    sum = 0
    for i in range(m):
        sum = sum + x[i]**n
    return (sum)
