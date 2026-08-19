#1 海尔洗衣机
class Washer:
     #构造函数：初始化宽度+高度
    def __init__(self,width,height):
        self.width=width
        self.height=height

     #定义功能方法(实例方法)
    def fuction(self):
        print("功能是洗衣服")
    
  #创建海尔洗衣机对象
haier_washer=Washer(500,800)

print(f"海尔洗衣机的宽是{haier_washer.width},高是{haier_washer.height}")
haier_washer.fuction()

#2 动物吃吃吃
class animal:
    def call(self):
        print("动物会叫")
    def feed(self):
        print("动物会吃")

Anim=animal()

Anim.call()
Anim.feed()

#3 圆⚪
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def get_area(self):
        return 3.14*(self.radius**2)#面积公式

try:
    r=float(input("请输入圆的半径："))
    circle=Circle(r)
    area=circle.get_area()
    print(f"圆的面积{area:.2f}")

except ValueError:
    print("输入无效，请输入一个有效的数字")

#4 设计课程类
class Lesson:
    def __init__(self,course_id,course_name,teacher,location):
        self.course_id=course_id
        self.course_name=course_name
        self.teacher=teacher
        self.__location=location #私有

    def display(self):
        print(f"课程编号：{self.course_id}")
        print(f"课程名称：{self.course_name}")
        print(f"任课教师：{self.teacher}")
        print(f"上课地点：{self.__location}") #类内部可访问私有属性

my_course=Lesson("001", "Python 程序设计", "张小红", "B 栋 103")
my_course.display()

#5 哟哟煎饼果子来一套
class Master:

#如果属性是固定的（如本题的“祖传”）：不要写参数，直接在函数体内赋值
#如果属性是灵活的（比如每个人的名字不一样）：才需要写参数，并且在函数体内使用 self.kongfu = kongfu 来接收外部传入的值。
    def __init__(self): #无参数
        self.kongfu="祖传煎饼锅"
        self.recipe="秘制煎饼果子配方"
    
    def make_cake(self):
        print(f"{self.kongfu}不外传")
        print(f"{self.recipe}传给徒弟")

class tudi(Master):
    pass # 使用 pass 表示直接继承父类的所有功能，无需额外代码

Tu=tudi()
Tu.make_cake()

#6 人和马的吃和睡
 #定义原始
class Base:
    def eat(self):
        pass
    def sleep(self):
        pass
 
 #重写：人
class Person(Base):
    def eat(self):
        print("人吃蔬菜水果肉")
    def sleep(self):
        print("人躺着睡觉")
 #重写：马
class Horse(Base):
    def eat(self):
        print("马吃草料")
    def sleep(self):
        print("马也躺着睡觉")    

class Action: #多态调用者
    def __init__(self,obj):
        self.obj=obj

    def do_action(self):
        self.obj.eat()
        self.obj.sleep()

#创建具体对象
p=Person()
h=Horse()

#将人对象传入
action_person=Action(p)
action_person.do_action()
#将马对象传入
action_hourse=Action(h)
action_hourse.do_action()
