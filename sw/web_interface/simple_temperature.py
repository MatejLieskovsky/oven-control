from oven_data import OvenStatusIn, OvenHeatingOut 

class SimpleTemperature(object):
	def __init__(self):
		self.temp = None
	
	def set_temp(self,temperature):
		self.temp = temperature
	
	def get_heating(self,data):	 
		out = OvenHeatingOut()
		if data.temp > self.temp:
			return out
		if data.temp < (self.temp - 15):
			out.top_big = True
			out.top_small = True
			out.bottom = True
			return out
		if data.temp < (self.temp - 5):
			out.top_small = True
			out.bottom = True
			return out
		return out
