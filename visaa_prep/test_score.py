n,x,y = map(int,input().split())
if (n >= y//x) and (y % x == 0):
    print("YES")
else:
    print("NO")
