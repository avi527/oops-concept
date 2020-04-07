class Rectangle:
	def __init__(self,length,width):
		self.length=length
		self.width=width
	def Area(self):
		print("area")
		areaOut=self.length * self.width
		return areaOut
	def Perimeter(self):
		return 2*self.length + 2*self.width
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
class Cube(Square):
    def surface_area(self):
        face_area = super().Area()
        return face_area * 6
    def volume(self):
        face_area = super().Area()
        return face_area * self.length

R=Rectangle(2,3)
print(R.Area(),R.Perimeter())

s=Square(6)
print(s.Area(),s.Perimeter())

cube = Cube(3)
print(cube.surface_area())
print(cube.volume())