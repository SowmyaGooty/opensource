t = int(input())
for i in range(t):
    n,m = list(map(int,input().split( )))
    if n>m:
        print(n-m)
    elif n<=m:
        print("0")
