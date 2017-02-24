# Is-a, Has-a, Objects, and Classes

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is an Animal
class Dog(Animal):
	def __init__(self, name):
		## Dog has a name
		self.name = name
