
"""Is-a, Has-a, Objects, and Classes"""


# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass


class Dog(Animal):  # Dog is an Animal
    def __init__(self, name):
        # Dog has a name
        self.name = name


class Cat(Animal):
    def __init__(self, name):
        self.name = name


class Person(object):
    def __init__(self, name):
        self.name = name
        # Person  has-a pet of some kind
        self.pet = None


class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary


class Fish(object):
    pass


class Salmon(Fish):
    pass


class Halibut(Fish):
    pass


# use the classes
rover = Dog("Rover")
satan = Cat("Satan")
mary = Person("Mary")
mary.pet = satan
frank = Employee("Frank", 120000)
frank.pet = rover
flipper = Fish()
crouse = Salmon()
harry = Halibut()
