import services

class Registry:
	def __init__(self):
		self.service_map = {}
		self.service_map['so'] = services.ServiceOne()
		self.service_map['st'] = services.ServiceTwo()
		
	def get_service(self,service_name):
		return self.service_map[service_name]