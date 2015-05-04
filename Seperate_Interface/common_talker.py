import sys
sys.path.insert(0, '/..')

import yeller.yeller

#Access to a different package. In this case, just a silly file that prints stuff
class CommonTalker:
	def __init__(self):
		self.y = yeller.yeller.YellsThings()

	def create(self,query):
		self.y.yell_this(query)
		
	def read(self):
		return self.y.pick_up_noise()
	
	def update(self,query):
		self.y.yell_this(query)
		
	def delete(self,query):
		self.y.yell_this(query)