x = input()
c = 1
res = ""
for i in range(len(x) - 1):
    if x[i] != x[i+1]:
        res += x[i] + str(c)
        c = 1
    else:
        c += 1
res += x[-1] + str(c)
print(res)
    
