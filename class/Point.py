class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)

    def __div__(self, other):
        return Point(self.x / other, self.y / other)

    def __truediv__(self, other):
        return Point(self.x / other, self.y / other)

    def __floordiv__(self, other):
        return self.x // other, self.y // other

    def __mod__(self, other):
        return Point(self.x % other.x, self.y % other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return "Point({0}, {1})".format(self.x, self.y)


p1 = Point(1, 2)
p2 = Point(2, 3)
p3 = Point(2, 3)

print("Points", str(p1), "&", str(p2), "are equal:", p1 == p2)
print("Points", str(p2), "&", str(p3), "are equal:", p2 == p3)
print("Points", str(p1), "+", str(p2), "are:", p1 + p2)
print("Points", str(p1), ">=", str(p2), "are:", p1 >= p2)
