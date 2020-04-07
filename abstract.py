# we use interface when all the feature need to be implemented differently for different object
from abc import ABC,abstractmethod

class Father(ABC):
	@abstractmethod
	def disp(self):
		pass
class Child(Father):
	def disp(self):
		print("child class")
		print("defining abstract method")
c=Child()
c.disp()
print("-----------------------------------------------------------------------------")

class Father(ABC):
	@abstractmethod
	def disp1(self):
		pass
	@abstractmethod
	def disp2(self):
		pass
class Child(Father):
	def disp1(self):
		print("child class")
		print("disp 1 abstract method")
class Grandchild(Child):
	def disp2(self):
		print("Grandchild class")
		print("disp2 abstract method")

gc=Grandchild()
gc.disp1()
gc.disp2()
print("------------------------------------------------------------------------------")

# Abstract Properties :
# Abstract classes includes attributes in addition to methods, you can require
# the attributes in concrete classes by defining them with @abstractproperty.

class Animal(ABC): 
    @abstractmethod
    def move(self): 
        pass
class Human(Animal): 
    def move(self): 
        print("I can walk and run") 
  
class Snake(Animal): 
    def move(self): 
        print("I can crawl") 
  
class Dog(Animal): 
    def move(self): 
        print("I can bark") 
  
class Lion(Animal): 
    def move(self): 
        print("I can roar") 
  
c=Human()
c.move() 














