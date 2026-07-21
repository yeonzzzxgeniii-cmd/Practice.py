#1 小明买书
A=100
B=35*0.8

print(f"小明还剩{A - B:.2f}元") 
#f-string 
#在引号前加 f，告诉 Python 这是一个格式化字符串，可以直接在里面嵌入变量或算式。
#.2f表示保留两位小数

print("小明还剩{:.2f}元".format(A - B))
#.format() 

print("小明还剩 %.2f 元" % (A - B))
# %占位符
# %f 代表浮点数，.2 代表保留两位

#2 a、b互换
a=100
b=200
print(f"交换前a是{a}，b是{b}")

a,b=b,a
#应用：打包元组
print(f"交换后a是{a}，b是{b}")

#拓展：冒泡排序
numbers=[5,3,8,6,7,2,4,1]
print(f"排序前的列表是{numbers}")

for i in range(len(numbers)-1):
    for j in range(len(numbers)-1-i):
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]

print(f"排序后的列表是{numbers}")

#3 牛吃草
#假设1头牛1天吃1份草
cows1=15
days1=20
total_grass=cows1*days1

cows2=20
days2=10
total_grass2=cows2*days2

new_grass_per_day=(total_grass-total_grass2)/(days1-days2)
print(f"每天新长的草可供{new_grass_per_day:.2f}头牛吃一天")

#4 温度
tem=float(input("请输入你的体温（摄氏度）："))
a=tem+272.15
print(f"{tem}摄氏度对应的华氏度为：{a:.2f}")

#5 年转换算天数
year=int(input("请输入年份："))
month=int(input("请输入月份："))
if year%4==0 and year%100!=0 or year%400==0:
    if month==2:
        print(f"{year}年{month}月的天数是：29天")
    elif month in [1,3,5,7,8,10,12]:
        print(f"{year}年{month}月的天数是：31天")
    else:
        print(f"{year}年{month}月的天数是：30天")

#6 快递收费
length=float(input("请输入快递的长度（米）："))
wide=float(input("请输入快递的宽度（米）："))
height=float(input("请输入快递的高度（米）："))
weight=float(input("请输入包裹重量（千克）："))
if length>1 or wide>1 or height>1 or weight>40:
    print("快递不符合要求，无法寄送")
else:
    base_fee=5
    if weight<10:
        total_fee=base_fee+1.5
    elif 10<=weight<30:
        total_fee=base_fee+2.0
    else:
        total_fee=base_fee+2.5
    
print(f"快递的总费用为：{total_fee:.2f}元")

#7 折纸比珠峰
paper_thickness=0.03
mountain_height=8848.86*1000

folds=0
while paper_thickness<mountain_height:
    paper_thickness*=2
    folds+=1

print(f"需要折叠 {folds} 次才能达到珠峰的高度")
print(f"折叠后的纸张厚度为：{paper_thickness:.2f}米")

#8用户猜测
import random
num=random.randint(1,20)
for i in range(3):
    guess=int(input("请输入你猜测的数字（1-20）："))
    if guess==num:
        print("恭喜你，猜对了蒸蚌！")
        break
    elif guess<num:
        print("太小了，请重新输入：")
    else:
        print("太大了，请重新输入：")
else:
    print(f"很遗憾，你没有猜对，正确的数字是：{num}")