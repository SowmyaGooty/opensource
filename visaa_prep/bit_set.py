n = int(input())
i = int(input())
res = 1<<(i-1)
if (n & res) != 0:
    print("true")
else:
    print("false")
