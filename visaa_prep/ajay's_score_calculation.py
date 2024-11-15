t = int(input())
for i in range(t):
    x,n = list(map(int,input().split()))
    s = (x//10) * n
    print(s)
