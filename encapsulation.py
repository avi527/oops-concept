#protect member
class Base:
	def __init__(self):
		#protected member 
		self._a=2
class Derived(Base):
	def __init__(self):
		#calling constructor of base class
		Base.__init__(self)
		print("base class protected member")
		print(self._a)
d=Derived()

#protected member
# Python program to  
# demonstrate private members 
  
# Creating a Base class 
class Base: 
    def __init__(self): 
        self.a = "Avinash"
        self.__c = "Avinash singh"
        print(self.__c)
  		
# Creating a derived class 
class Derived(Base): 
    def __init__(self): 
          
        # Calling constructor of 
        # Base class 
        Base.__init__(self)  
        print("Calling private member of base class: ") 
        print(self.__a) 
# Driver code 
obj1 = Base() 
print(obj1.a) 