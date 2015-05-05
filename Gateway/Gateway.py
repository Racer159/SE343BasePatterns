import SomeData

class Gateway:

	def __init__(self):
		self.data = SomeData.SomeData()

	def getMathy(self):
		return self.data.MathyData

	def getWordy(self):
		return self.data.WordyData

	def getTruthy(self):
		return self.data.TruthyData

	def getFunctionality(self):
		return self.data.functionality()