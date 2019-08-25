from random import randint
class Tiger:	
	def __init__(self):
		self.age = 0
		self.LIFE_TIME = 23
		self.survive = True
		self.hunger = 0
		self.sex = randint(0,1) #0雄1雌
	def newYear(self):
		self.age += 1
		self.hunger += 1
		if self.age == self.LIFE_TIME:
			self.survive = False
	def eat(self):
		self.hunger = 0