# Object:- object cantain attributes  and behaviours
# class:- class can define attributes  and behaviours of all the object
# method:- object have attributes  and behaviours these are called method in programming

# Example:-
# class => Human
# attributes => name,age,color
# behaviour => eating

class Humans():
	#class Attribute
	def __init__(self,name,age,color):
		self.name=name
		self.age=age
		self.color=color
	def Eating(self):
		print(f"{self.name} eating meals")
h1=Humans('avinash','25','white')
h1_method=h1.Eating()

class Human():
	#class Attribute
	def __init__(self,name,height,weight):
		self.name=name
		self.height=height
		self.weight=weight
		# object behaviour method
	def Eating(self,food):
		return "{} is eating {}".format(self.name,food)

# Access Object
ram = Human("Ram", 6, 60)
print(ram.__dict__)
steve = Human("Steve", 5.9, 56)
print(steve.__dict__)
print("{} height is {} and weight is {} {}".format(ram.name,ram.height,ram.weight,'---',ram.Eating('pizza')))
print("{} height is {} and weight is {} {}".format(steve.name,steve.height,steve.weight,'---',steve.Eating('pizza')))



class Myclass():
	#instance attribute
	num=20
	#instance method
	def Hello(self):
		print("hello python")
obj=Myclass()
print(obj.num)
obj.Hello()

class employee():
    def __init__(self,name,age,id,salary):  
        self.name = name 
        self.age = age
        self.salary = salary
        self.id = id
 
emp1 = employee("harshit",22,1000,1234) 
emp2 = employee("arjun",23,2000,2234)
print(emp2.__dict__)