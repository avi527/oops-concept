class Tomato:
	def type(self):
		print("vegitable")
	def color(self):
		print("red")
class Apple:
	def type(self):
		print("fruit")
	def color(self):
		print("red")

def function(veg):
	veg.type()
	fruit.color()

veg=Tomato()
veg.type()
veg.color()
fruit=Apple()
fruit.type()
fruit.color()
function(veg)
function(fruit)


class India():
     def capital(self):
       print("New Delhi")
 
     def language(self):
       print("Hindi and English")
 
class USA():
     def capital(self):
       print("Washington, D.C.")
 
     def language(self):
       print("English")
 
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
	country.capital()
	country.language()

#polymorphism with inheritance

class Bird:
     def intro(self):
       print("There are different types of birds")
 
     def flight(self):
       print("Most of the birds can fly but some cannot")
 
class parrot(Bird):
     def flight(self):
       print("Parrots can fly")
 
class penguin(Bird):
     def flight(self):
       print("Penguins do not fly")
 
obj_bird = Bird()
obj_parr = parrot()
obj_peng = penguin()
 
obj_bird.intro()
obj_bird.flight()
 
obj_parr.intro()
obj_parr.flight()
 
obj_peng.intro()
obj_peng.flight()	