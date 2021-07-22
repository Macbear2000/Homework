#研究生绩点计算
a = int(input('请输入你的成绩'))
if a>=95 and a<=100:
    print('你的成绩为A或者A+，绩点为4.0')
elif a>=90 and a<=94:
    print('你的成绩为A-，绩点为3.7')
elif a>=85 and a<=89:
    print('你的成绩为B+，绩点为3.3')
elif a>=80 and a<=84:
    print('你的成绩为B，绩点为3.0')
elif a>=77 and a<=79:
    print('你的成绩为B-，绩点为2.7')
elif a>=73 and a<=76:
    print('你的成绩为C+，绩点为2.3')
elif a>=70 and a<=72:
    print('你的成绩为C，绩点为2.0')
elif a>=67 and a<=69:
    print('你的成绩为C-，绩点为1.7')
elif a>=63 and a<=66:
    print('你的成绩为D+，绩点为1.3')
elif a>=60 and a<=62:
    print('你的成绩为D，绩点为1.0')
elif a>=0  and a<=59:
    print('很遗憾，你挂科了')