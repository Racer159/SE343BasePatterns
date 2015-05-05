import common_talker

#Interface with common_talked with limited functionality
class GeneralBroadcaster:
	def __init__(self):
		self.mic = common_talker.CommonTalker()
	
	def say_something(self, something):
		self.mic.create(something)