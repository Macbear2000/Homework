#输出九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        a = i*j
        print('%dx%d=%d\t'%(j,i,a),end ='')
    print()