n = int(input())
arr = list(map(int,input().split( )))
a = arr[1:] + arr[:1]
for i in range(len(a)):
    print(a[i], end=" ")
