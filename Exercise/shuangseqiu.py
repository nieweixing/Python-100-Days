#双色球的下注随机选号

import random

red_ball=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
blue_ball=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
num=int(input('请输入你要下注的数量:'))
for i in range(num):
    Order_red=random.sample(red_ball, 6)
    Order_blue=random.sample(blue_ball, 1)
    print("第%d注下注的红色球号码为:" %(i+1),Order_red)
    print("第%d注下注的蓝色球号码为:" %(i+1),Order_blue)