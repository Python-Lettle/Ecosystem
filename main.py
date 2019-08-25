#coding:utf-8
import time
from random import randint
from Bionts.Grass import Grass
from Bionts.Rabbit import Rabbit
from Bionts.Tiger import Tiger

global Years,tigers,rabbits
Years = 1
tigers = []
rabbits = []
Start = True

#输入基数 传参
ret = input("基数(草,兔子,老虎):")
spliter = ret.split(",")
for i in range(int(spliter[2])):
	tigers.append(Tiger())
for i in range(int(spliter[1])):
	rabbits.append(Rabbit())
Grass = Grass(int(spliter[0]))

def infoPrint():
	print("现在是第{0}年,地面上有{1}棵草,有{2}只兔子,有{3}只老虎.".format(Years,Grass.amount,str(len(rabbits)),str(len(tigers))))

def nextYear():
	global Years,tigers,rabbits
	Years += 1
	propagate_num = 0
	def propagate(mob,num):
		mobs = []
		for i in range(num):
			mobs.append(mob())
		return mobs
	#关于老虎的 饱食度 寿命 繁殖
	for i in tigers:
		i.newYear()
		if i.hunger == 3:
			i.eat()
			n = randint(0,len(rabbits)-1)
			del rabbits[n]
		if not i.survive:   #自然死亡
			tigers.remove(i)
		elif i.age == 12:   #繁殖计数
			propagate_num += 1
	tigers += propagate(Tiger,int(propagate_num/2))
	propagate_num = 0
	#关于兔子的 寿命 繁殖
	for i in rabbits:
		i.newYear()
		if not i.survive:
			rabbits.remove(i)
		elif i.age == 2 or i.age == 3 or i.age == 4 or i.age == 6:
			propagate_num += 1
	rabbits += propagate(Rabbit,int(propagate_num/2))
	propagate_num = 0
	Grass.eaten(len(rabbits))
	Grass.grow()

while Start:
	infoPrint()
	nextYear()
	time.sleep(1)
	if not (len(tigers)>0 and Grass.amount>0 and len(rabbits)>0):
		Start = False