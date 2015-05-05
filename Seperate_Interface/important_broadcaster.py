import common_talker

#Interface with common_talker using more functionality
class ImportantBroadcast:
	def __init__(self):
		self.mic = common_talker.CommonTalker()
		
	def say(self,message):
		self.mic.create(message)
		
	def get_feedback(self):
		return self.mic.read()
		
	def ammend_message(self,message):
		self.mic.update(message)
		
	def take_it_back(self,message):
		self.mic.delete(message)