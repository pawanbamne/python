
class person:
	"""docstring for ClassName"""
	def __init__(self, name, age):
		self.name = name
		self.age = age
p1 = person("john", 36)

print(p1.name)
print(p1.age)
		

class person:
	"""docstring for ClassName"""
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def myfunc(self):
		print("hello name is "+ self.name)
		
p1 = person("john", 36)
p1.myfunc()





