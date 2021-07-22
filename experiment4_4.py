count = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and i!=k and j!=k:
                a=str(i)
                b=str(j)
                c=str(k)
                ret = a+b+c
                print(ret)
                count+=1
print('一共有%d个组合'%(count))
