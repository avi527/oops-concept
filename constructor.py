# A constructor is special kind of method.it is used for intitalize instanse
# variable during the object creation
# type:-
# 1.default
# 2.parameterized
class Democonst():
	#constructor
	def __init__(self):
		#instanse variable
		self.num=100
		#create method
	def read_num(self):
		print(self.num)

#object creation
d=Democonst()
#calling method
d.read_num()

#without constructor body (default constructor)
class WithoutConsBody():
	num=101
	def ReadNum(self):
		print(self.num)
wcb=WithoutConsBody()
wcb.ReadNum()

#When we declare a constructor
class DemoClass:
    num = 101
    # non-parameterized constructor
    def __init__(self):
        self.num = 999
    # a method
    def read_number(self):
        print(self.num)
# creating object of the class
obj = DemoClass()
# calling the instance method using the object obj
obj.read_number()


#Parameterized constructor
class DemoClass:
    num = 101
    # parameterized constructor
    def __init__(self, data):
        self.num = data
    # a method
    def read_number(self):
        print(self.num)
# creating object of the class
# this will invoke parameterized constructor
obj = DemoClass(55)
# calling the instance method using the object obj
obj.read_number()
# creating another object of the class
obj2 = DemoClass(66)
# calling the instance method using the object obj
obj2.read_number()
