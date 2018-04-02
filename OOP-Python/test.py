
class Call(object):
	def __init__(self,unique_id,caller_name,caller_phone,call_time,reason):
		self.unique_id = unique_id
		self.caller_name = caller_name
		self.caller_phone = caller_phone
		self.call_time = call_time
		self.reason = reason
	def display_call (self):
		print self.unique_id, self.caller_name, self.caller_phone, self.call_time, self.reason
		return self

class CallCenter (object):
	def __init__(self):
		self.calls = []
		self.queue_size = len(self.calls)
	def add(self, call):
		self.calls.append(call)
		self.queue_size = len(self.calls)
	def remove(self):
		self.calls.pop(0)
		self.queue_size = len(self.calls)
	def info(self):
		for callz in self.calls:
			print callz.caller_name, callz.caller_phone
	def remove_by_number(self,number):
		for i in range (len(self.calls)):
			if self.calls[i].caller_phone == number:
				self.calls.pop(i)
		self.queue_size = len(self.calls)

CC = CallCenter()

CC.add(Call(1,'sam','408-911-9099','4pm','catching up'))
CC.add(Call(1,'tejas','408-386-1914','5pm','remindinf you :)'))

CC.info()

CC.remove()

CC.info()

