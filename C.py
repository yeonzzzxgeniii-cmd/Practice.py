#1 下午茶套餐搭配
drink_list=["咖啡","橙汁","红茶"]
eat_list=["松饼","提拉米苏","芝士蛋糕","三明治"]

print("下午茶套餐搭配如下：")
for drink in drink_list:
    for eat in eat_list:
        print(f"{drink} + {eat}")

#2 注册登录
#第一步:要先初始化列表
account_list = [] 
password_list = []

print("******************")
print("*  模拟注册登录   *")
print("******************")

#第二步：让程序一直运行（无限循环）
while True:
    print("\n1-注册\n2-登录\n3-退出")
    choice = input("请输入你的选择:")
    if choice == "1":
        new_account = input("请输入新账号:")
        if new_account in account_list:
            print("该账号已存在，请重新输入！")
        else:
            new_password = input("请输入新密码:")
            confirm_password = input("请再次输入新密码:")
            if new_password == confirm_password:
                account_list.append(new_account)
                password_list.append(new_password)
                print("注册成功！")
            else:
                print("两次输入的密码不一致，请重新注册！")
    
    elif choice == "2":
        login_account = input("请输入账号:")
        if login_account not in account_list:
            print("该账号不存在，请先注册！")
        else:
            login_password = input("请输入密码:")
            index = account_list.index(login_account)
            if login_password == password_list[index]:
                print("登录成功！")
            else:
                print("密码错误，请重新输入！")

    elif choice == "3":
        print("退出程序！")
        break

    else:
        print("无效的选择，请重新输入！")

#3 商城购物
# 初始设置
goodsstup = (
    ('0', '巨无霸白桃', 10), 
    ('1', '阳光葡萄玫瑰', 15),
    ('2', '五香牛肉', 100), 
    ('3', '红颜牛奶草莓', 20), 
    ('4', '农家散养土鸡蛋', 6)
)
n = len(goodsstup)
money = 100
total = 0          # 【隐患修复1】：将 sum 改为 total，避免覆盖 Python 内置的 sum() 函数
cart = []          # 【新增功能】：使用一个列表来记录购物清单

# 页面设计
print("*" * 20)
print("*   商城购物   *")
print("*" * 20)
print("1-浏览商品信息")
print("2-购买商品")
print("3-余额充值")
print("4-结算金额")
print("5-退出系统")
print("*" * 20)

# 功能
while True:
    try:  # 【隐患修复2】：增加 try-except 捕获 ValueError，防止输入字母导致程序崩溃
        choose = int(input("请输入你的选择: "))
        
        if choose == 1:
            print("\n~~商品信息~~")
            print("编号\t\t商品\t\t\t价格（元/斤）")
            for i in range(n):
                print(f"{goodsstup[i][0]:<2}\t\t{goodsstup[i][1]:<10}\t\t{goodsstup[i][2]:<2}")
        
        elif choose == 2:
            print("\n~~购买商品~~")
            while True:
                id = int(input("请输入商品编号: "))
                if id < 0 or id >= n:
                    print("❌ 商品编号不存在，请重新输入！")
                    continue 
                
                num = int(input("请输入购买数量(斤): "))
                # 将购买的商品信息追加到购物车中
                cart.append((goodsstup[id][1], num, goodsstup[id][2])) 
                total += num * goodsstup[id][2]
                
                flag = input("是否继续购买？(y/n): ")
                if flag.lower() == "n":  # 使用 .lower() 兼容大小写
                    break
        
        elif choose == 3:
            print("\n~~余额充值~~")
            print(f"当前余额为：{money}元")
            m = float(input("请输入充值金额: "))
            money += m
            print(f"✅ 充值成功，当前余额为：{money}元")

        elif choose == 4:
            print("\n~~结算金额~~")
            #空列表 [] 会被自动判定为假（False），而非空列表（里面有东西）会被判定为真（True）
            if not cart:  # 如果购物车是空的，提示用户先去购物
                print("您的购物车是空的，请先去购物哦！")
            else:
                print("🧾 您的购物清单如下：")
                print("-" * 30)
                print(f"{'商品名称':<12}{'数量':<6}{'单价':<6}{'小计'}")
                for item in cart:
                    name, num, price = item #解包
                    print(f"{name:<12}{num:<6}{price:<6}{num * price}元")
                print("-" * 30)
                print(f"总计消费：{total}元")
                
                if total > money:
                    print("❌ 余额不足，请先充值！")
                else:
                    money -= total
                    print(f"✅ 结算成功，扣除 {total}元，当前余额为：{money}元")
                    total = 0  # 【隐患修复4】：结算成功后必须将消费总额清零，防止下次重复扣费
                    cart = []  # 同时清空购物车清单
        
        elif choose == 5:
            print("👋 退出系统！欢迎下次光临！")
            break     
        
        else:
            print("⚠️ 无效的选择，请重新输入！")
            
    except ValueError:
        print("⚠️ 输入有误，请输入有效的数字！")

#4 扑克牌
#花色
suits = ['♠', '♥', '♦', '♣']
#点数（13张）
ranks = [ '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A','2']
#生成整幅扑克牌
'''等同于：
deck_list = []
for rank in ranks:          # 外层循环：遍历 13 个点数
    for suit in suits:      # 内层循环：对每个点数，遍历 4 个花色
        deck_list.append((suit, rank))  # 组合成元组，比如 ('♠', '3')'''
#[最终要装进列表的东西 + 外层循环 + 内层循环]
#原代码：rank在外suit在内，生成列表为先优先找齐一个数的所有花色
#如果是suit在外rank在内，生成列表为先优先找齐一个花色的所有数   
deck_list=[(suit, rank) for rank in ranks for suit in suits]

#用元组封装锁死
deck_tuple=tuple(deck_list)
print(deck_tuple)

#5阶梯式奖金[yun]
#<1>定义元组
threshold = (100000, 200000, 400000, 600000, 1000000)
rate = (0.1, 0.075, 0.05, 0.03, 0.015, 0.01)

#<2>获取输入
profit = int(input("请输入当月利润（元）："))

#<3>计算奖金
bonus = 0
remaining_profit = profit
for i in range(len(threshold)):
    limit = threshold[i]
    if remaining_profit <=limit:
        bonus += remaining_profit * rate[i]
        remaining_profit = 0
        break
    else:
        bonus += limit * rate[i]
        remaining_profit -= limit

if remaining_profit > 0:
    bonus += remaining_profit * rate[-1]

#<4>输出结果
print(f"应发放奖金总数(元)：{int(bonus)}")

#6 判断回文
s=input("请输入字符串：")
#反转：步长取-1
if s==s[::-1]:
    print(f"{s}是回文")
else:
    print("不是回文")

#7 屏蔽不文明
negative={"傻逼","sb","垃圾","滚","妈的","操你妈"}
flag=0 #标志位思想：记录状态，延迟处理
contents=input("请输入评论内容：")
for i in negative:
    if i in contents:
        flag=1
        contents=contents.replace(i,"*"*len(i))
if flag==1:
    print("评论内容不文明，已屏蔽")
    print(contents)

#8 学生选课登记后台设置
history_course = {'小明','张三','李四','王五','Lily','Bob'}
music_course = {'小明','张三','小红','王强'}
art_course = {'小明','Bob','Jack','李四','Lily'}

#用并集统计不重复学生
all_students = history_course | music_course | art_course
print(f"总共有{len(all_students)}名学生选课")

#用差集找出在历史课名单但不在另外两个的学生
only_history_students = history_course - music_course - art_course
print(f"只选历史课的学生的人数为：{len(only_history_students)}")

# 初始化统计学生选课次数的字典（新增这一行！）
student_courses_count = {}

#遍历进行统计
for student in history_course:
    student_courses_count[student] = student_courses_count.get(student, 0) + 1 #字典中内置方法，0为设置默认值，防止键不存在出现问题
for student in music_course:
    student_courses_count[student] = student_courses_count.get(student, 0) + 1  
for student in art_course:
    student_courses_count[student] = student_courses_count.get(student, 0) + 1

#根据计数结果，将学生分类到不同集合中
one_course_students = set()
two_course_students = set()
three_course_students =set()

for student, count in student_courses_count.items():
    if count == 1:
        one_course_students.add(student)
    elif count == 2:
        two_course_students.add(student)
    elif count == 3:
        three_course_students.add(student)

print(f"只选一门课的学生人数为：{len(one_course_students)}")
print(f"姓名：{one_course_students}")
print(f"选两门课的学生人数为：{len(two_course_students)}")  
print(f"姓名：{two_course_students}")
print(f"选三门课的学生人数为：{len(three_course_students)}")
print(f"姓名：{three_course_students}")

#9 问卷调查抽取去重
import random
n=int(input("请输入本次问卷调查人数："))

student_ids = set()  # 使用集合去重
while len(student_ids) < n:
    num=random.randint(1, 1000) 
    student_ids.add(num)

sorted_ids = sorted(student_ids)  # 排序
print(f"本次问卷调查学生学号为：{sorted_ids}")

#10 电子记账本
#从 Python 的高级数据工具箱（collections）里，把 defaultdict 字典工具拿出来，放到我当前的代码里准备使用
from collections import defaultdict

#用float原因；这个字典里的金额，请默认给我准备一个 0.0 的起点，方便我随时把新输入的小数价格加上去
item =defaultdict(float)
total_amount=0.0

while True:
    name=input("商品名称:")
    price=float(input("商品金额："))
    item[name]+=price
    total_amount+=price
    choice=input("是否继续录入？(y/n):")
    if choice.lower() != 'y':
        break
    print("您本次购物详单如下：")
    for name, price in item.items():
        print(f"{name}: {price:.1f}元")

print(f"总金额：{total_amount:.1f}元")  

#11 统计字母出现次数
str='skdaskerkjsalkj'
#初始化字典
letter_count = {}

for char in str:
    if char in letter_count:
        letter_count[char] += 1
    else:
        letter_count[char] = 1

print(letter_count)



 