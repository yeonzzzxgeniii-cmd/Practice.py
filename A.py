import random
def Lotto():#定义一个双色球函数
    red=[]
    for r in random.sample(range(1,34),6):#range前开后闭，r为red里的数
        red.append(str(r))#追加6个整数到红球列表
    
    blue=str(random.randint(1,16))

    return ' '.join(red)+' '+ blue#用空格连接所有红球号码

#如果是主程序，用' '来变成字符串来进行比对
    #__name__ 为默认生成身份证，后台给__name__默认的赋值就是'__main__'
    #现在为判断条件：如果赋值是'__main__'就·····
if __name__ == '__main__':
   print('双色球的中奖号码为：',Lotto())

 