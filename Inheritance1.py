class Animal:  
    def speak(self):  
        print("Animal Speaking")  
#child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
d = Dog()  
d.bark()  
d.speak()
# a=Animal()
# a.speak()

# parent class 
class Person( object ):     
  
        # __init__ is known as the constructor          
        def __init__(self, name, idnumber):    
                self.name = name 
                self.idnumber = idnumber 
        def display(self): 
                print(self.name) 
                print(self.idnumber) 
  
# child class 
class Employee( Person ):            
        def __init__(self, name, idnumber, salary, post): 
                self.salary = salary 
                self.post = post 
                print(name)
                print(idnumber)
                print(salary)
                print(post)
  				
                # invoking the __init__ of the parent class  
                Person.__init__(self, name, idnumber)  
  
                  
# creation of an object variable or an instance 
a = Person('Rahul', 886012)     
  
# calling a function of the class Person using its instance 
a.display()  
b=Employee('dev',30,20,'devff')
