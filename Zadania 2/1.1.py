# Okrąg, kwadrat - bok, promień, średnica, obwód,  pole
import math
# class Figure:



class Circle:
    def __init__(self, radius=1):
        if radius != 1:
            self.radius = radius
        else:
            self.radius = 1
    def __str__(self):
        return f"Circle, radius: {self.__radius}, diameter: {self.diameter}, area:  {self.area}"

    def __add__(self, other):
        c=Circle()
        c.area = self.area + other.area
        return c



    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self.__radius = value

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * (self.radius**2)
    @area.setter
    def area(self, value):
        self.radius = (value / math.pi) ** (1 / 2)



class Square:
    def __init__(self, side=1):
        if side != 1:
            self.side = side
        else:
            self.side = 1
    def __str__(self):
        return f"Square, side: {self.side}, circuit: {self.circuit}, area: {self.area}"

    def __add__(self, other):
        s=Square()
        s.area = self.area + other.area
        return s

    @property
    def circuit(self):
        return self.side * 4
    @circuit.setter
    def circuit(self, value):
        self.side = value / 4
    @property
    def area(self):
        return self.side **2
    @area.setter
    def area(self, value):
        self.side = value ** (1/2)

s = Square(2)
c = Circle(2)

print(s, c)
print(s+c)
print(c+s)


s = Square(2)
print(s)
s.circuit = 100
print(s.side, s.circuit, s.area)
print(s)






c = Circle()
print(c)
print(c.radius, c.diameter, c.area)
c = Circle(2)
print(c.radius, c.diameter, c.area)
c.radius = 3
print(c.radius, c.diameter, c.area)
a = Circle(4)
b = Circle(3)

print(a+b)
print(c+s)
