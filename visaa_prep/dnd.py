m,n  = map(int,input().split())
x = list(map(int,input().split()))
num1 = 0
num2 = 0
for i in x:
    if (i % n == 0):
        num2 += i        
    else:
        num1 += i
print(num2 - num1)
