import math


class Circle:
    def __init__(self, radius=1):
        if radius != 1:
            self.radius = radius
        else:
            self.radius = 1

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
        x = math.pi * (self.radius**2)
        y = "{liczba:.3f}".format(liczba=x)
        return y

    @area.setter
    def area(self, value):
        self.radius = (value / math.pi) ** (1 / 2)


c = Circle()
print(c)
print(c.radius, c.diameter, c.area)
c = Circle(2)
print(c.radius, c.diameter, c.area)
c.radius = 3
print(c.radius, c.diameter, c.area)
