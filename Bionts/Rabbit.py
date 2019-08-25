from random import randint
class Rabbit:
	def __init__(self):
		self.age = 0
		self.LIFE_TIME = 8
		self.survive = True
		self.sex = randint(0,1)
	def newYear(self):
		self.age += 1
		if self.age == self.LIFE_TIME:
			self.survive = False