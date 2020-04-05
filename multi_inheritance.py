class Base1():
	def __init__(self):
		self.name="Avinash"
		print("base1 class")
class Base2():
	def __init__(self):
		self.sal="23000"
		print("base2 class")
class Derived(Base1,Base2):
	def __init__(self):
		Base1.__init__(self)
		Base2.__init__(self)
		print("Drived class")
	def GetName(self):
		print(self.name,self.sal)
mi=Derived()
mi.GetName()

print("-----------------------------------------------------")

class Base():
	def __init__(self,name,mobile):
		self.name=name
		self.mobile=mobile
	def GetDetail(self):
		return self.name,self.mobile

class Child(Base):
	def __init__(self,name,mobile,sal,post):
		Base.__init__(self,name,mobile)
		self.sal=sal
		self.post=post
	def Data(self):
		return self.name,self.sal,self.post

class GrandChild(Child):
	def __init__(self,name,mobile,sal,post,age):
		Child.__init__(self,name,mobile,sal,post)
		self.age=age
	def GetAllData(self):
		return self.age,self.name,self.mobile,self.sal,self.post
# b=Base('Avinash',8745016128)
# print(b.GetDetail())
b=GrandChild("Avinash",8745016128,40000,'Python dev',25)
print(b.GetAllData())