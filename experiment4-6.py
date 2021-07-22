#使用while循环改写阶乘运算
a = int(input('请输入数字n'))
ret = 1
while a>0:
    ret*=a
    a-=1
print(ret)