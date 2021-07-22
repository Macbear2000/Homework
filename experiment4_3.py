#获取数字n，并进行数字n的阶乘运算
a = int(input('请输入数字'))
ret = 1
for i in range(1,a+1):
    ret*=i

print(ret)