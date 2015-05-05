

class Record_Set:

	# Pretend that this class interacts with a relational database
	# instead of having hard coded data
	#
	# In a real example this would save changes back to the database
	# somewhere.

	def __init__(self):

		self.table = [[1,2,3],[4,5,6],[7,8,9]]

	def getTable(self):
		return self.table

	def setTable(self, table):
		self.table = table