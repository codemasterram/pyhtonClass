class Person:
	def __init__(self, name):
		self.name = name

	def say_hello(self):
		print('{} says hello'.format(self.name))
# p1 and p2 are the instances (object) or the class Person
p1 = Person('Foo')
p2 = Person('bar')

p1.say_hello()
p1.say_hello()


