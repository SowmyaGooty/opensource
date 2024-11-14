def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        x = 1
        for i in range(2,n+1):
            x *= i
        return x
n = int(input())
print(factorial(n))
