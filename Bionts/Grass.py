class Grass:
	def __init__(self,am):
		self.amount = am
	def eaten(self,amo):
		self.amount = self.amount - amo
	def grow(self):
		self.amount = int(self.amount*1.2)