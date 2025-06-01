def fib(n):
    if n <= 0:
        return
    elif n == 1:
        print(0)
        return
    
    a, b = 0, 1
    print(a, b, end =' ')

    for _ in range(2, n):
        c = a + b
        print(c, end=' ')
        a, b = b, c

n = int(input("Enter the no. of terms you want to print: "))
fib(n)