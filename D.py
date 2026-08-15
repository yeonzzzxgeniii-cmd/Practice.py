#1 角谷猜想
def fun(n):
    count=0
    
    while True:
        #偶数就n/2
        if n%2==0:
            n=n/2
            print(int(n),end=" ")
        #奇数就3n+1
        else:
            n=3*n+1
            print(int(n),end=" ")
        
        count+=1
        if n==1:
            print()
            break
    return count

n=int(input("请输入一个大于1的正整数:"))
print(f"{n}总共经过了{fun(n)}次运算变成1")

#2 判断能不能构成三角形的三条边
def fun(a,b,c):
    x,y,z=sorted([a,b,c])#sorted为从小到大

    if x>0 and x+y>z:
        print("可以构成三角形")
    else:
        print("很遗憾，不能构成三角形。。。")

#map:将读进来的那一堆“文本字符串”，一次性全部转换成“浮点数（小数）”。
a,b,c=map(float,input("请输入三角形的三条边长（用逗号分隔）：").split(","))
fun(a,b,c)

#3 饮料自动贩卖机
  #dict存储
drinks={"可口可乐":2.5,"冰红茶":3,
        "脉动":4,"绿茶":3,"尖叫":4}

#饮品信息显示
def show_drinks():
    print("\n---饮料列表---")
    for name,price in drinks.items():
        print(f"{name}:{price}yuan")
        print("---------------------")

#购买饮料
def buy_drinks():
    name=input("请输入你要购买的商品名称：")
    if name not in drinks:
        print("sorry，没有该饮料哦")
        return 0

    num=int(input("请输入购买数量："))
    return drinks[name]*num

#计算总价
def calc_total(money_list):
    return sum(money_list)

total_money=[]

while True:
    show_drinks()
    cost=buy_drinks()
     
    if cost>0:
        total_money.append(cost)
    
    choice=input("还买吗？（y/n)")
    if choice=='n':
        break

print(f"您购买饮品共花费{calc_total(total_money)}yuan")

#4 寻找质数
def fun():
    for n in range(2,101):
        is_prime=True #假设当前数字是质数
          #开始找茬
        for i in range(2,int(n**0.5)+1):
              #余数为0，说明找到了一个能整除它的数字
            if n%i==0:
                is_prime=False #说明不是质数
                break
        
        if is_prime==True:
            print(n,end=" ")

fun()

#5 加减分函数
  #加分
def add_score(current_score,add_value):
    return current_score+add_value

  #减分
def subtract_score(current_score,subtract_value):
    return current_score-subtract_value

score=int(input("请输入原始分数："))
input_str=input("请输入加/减分：")

if input_str.startswith('+'):
    val=int(input_str[1:]) #输入按索引切片【1】到结尾
    score=add_score(score,val)
elif input_str.startswith('-'):
    val=int(int_str[1:])
    score=substra_score(score,val)
else:
    val=int(input_str)
    score=add_score(score,val)

print(f"您最终分数是：{score}")

#6 完数  
  #外层实现指定范围
def find_perfact_num(start,end):
    #内层实现判断完数
    def is_perfect(n):
        return sum(i for i in range(1,n) if n%i == 0)==n #所有数相加之和
    return [num for num in range(start,end+1)if is_perfect(num)]

start,end=map(int,input("请输入范围（小-大，并用空格分开）：").split( ))
result=find_perfact_num(start,end) #把结果存进result里

#输出所有完数和个数
print(*result) #有*是解包，没*是打包
print(f'{start}-{end}共有{len(result)}个完数')

"""
* 就像是一个“打包单件的收纳袋”。
** 就像是一个“打包键值对的收纳袋”。
"""

#7 斐波那契 
#先定义
def fibonacci(n):
     if n==1 or n==2:
        return 1
     else:
        return fibonacci(n-1)+fibonacci(n-2)

#再调用
def fun(n):
    for i in range (1,n+1):
        print(fibonacci(i),end=" ")

n=int(input("要输入多少个数（>2）："))
fun(n)

#8 猴子吃桃子(真是馋的很。)
 #法1：循环 
def fun(n):
    peaches=1 # 第10天剩1个桃子（已知条件）

    # 循环往前推9天
    for i in range (1,n):
        peaches=(peaches+1)*2
    return peaches

total = fun(10)
print(f"猴子一天共摘了：{total}个桃子")

 #法2：用递推
def fun(n):
    if n==10:
        return 1 #出口
    else:
        return (fun(n+1)+1)*2

total=fun(1)
print(f"猴子一天共摘了：{total}个桃子")

"""
= 是赋值，给你
== 是比较，判断两边
"""

#9 年龄的秘密
def age(peo):
    if peo==1:
        return 10
    else:
        return age(peo-1)+2

result=age(5)
print(f'第五个人的年龄是：{result}')





    
    


 