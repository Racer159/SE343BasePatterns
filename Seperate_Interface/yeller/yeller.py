import random

class YellsThings:
	def yell_this(self,thing):
		print(thing.upper())
		
	def wisper_this(self,thing):
		print("*"+thing.lower()+"*")
		
	def yell_whatever(self):
		to_yell = ""
		for i in range(random.randint(0,20)):
			to_yell += chr(random.randint(65,91))
		print(to_yell)
		
	def pick_up_noise(self):
		return "Whisper wisper"