import math


class Figure:
    def __add__(self, other):
        c = self.__class__()
        c.area = c.area + other.area
        return c

    def __lt__(self, other):
        z = self.__class__()
        a = z.area < other.area
        return a

    def __le__(self, other):
        c = self.__class__()
        a = c.area <= other.area
        return a

    def __eq__(self, other):
        c = self.__class__()
        a = c.area == other.area
        return a

    def __ne__(self, other):
        c = self.__class__()
        a = c.area != other.area
        return a

    def __gt__(self, other):
        c = self.__class__()
        a = c.area > other.area
        return a

    def __ge__(self, other):
        c = self.__class__()
        a = c.area >= other.area
        return a


class Circle(Figure):
    def __init__(self, radius=1):
        if radius != 1:
            self.radius = radius
        else:
            self.radius = 1

    def __str__(self):
        return f"Circle, radius: {self.__radius}, diameter: {self.diameter}, area:  {self.area}"

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


class Square(Figure):
    def __init__(self, side=1):
        if side != 1:
            self.side = side
        else:
            self.side = 1

    def __str__(self):
        return f"Square, side: {self.side}, circuit: {self.circuit}, area: {self.area}"

    @property
    def circuit(self):
        return self.side * 4

    @circuit.setter
    def circuit(self, value):
        self.side = value / 4

    @property
    def area(self):
        return self.side**2

    @area.setter
    def area(self, value):
        self.side = value ** (1 / 2)


class Triangle(Figure):
    def __init__(self, side=1):
        if side != 1:
            self.side = side
        else:
            self.side = 1

    def __str__(self):
        return (
            f"Triangle, side: {self.side}, circuit: {self.circuit}, area: {self.area}"
        )

    @property
    def circuit(self):
        return self.side * 3

    @circuit.setter
    def circuit(self, value):
        self.side = value / 3

    @property
    def area(self):
        return ((self.side**2) * (3 ** (1 / 2))) / 4

    @area.setter
    def area(self, value):
        self.side = math.sqrt((4 * value) * (3 ** (1 / 2))) / 4
        # self.side = (value/s)/(s/(s+))


t = Triangle(2)
s = Square(3)
c = Circle(3)


print(s, t)
print(t + s)
print(s, c)
print(s + c)
print(c + s)

print(s, c)
print(c == s)
print(c >= s)
print(c <= s)
print(c != s)
print(c > s)
print(c < s)

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

print(a + b)
print(c + s)
