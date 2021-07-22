a=[0 for x in range(10)]
a[0] = 1
for i in range(1,10):
    a[i]=a[i-1]+1

print(a)