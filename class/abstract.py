from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def no_of_sides(self):
        pass


class Triangle(Polygon):
    def no_of_sides(self):
        return 3


class Square(Polygon):
    def no_of_sides(self):
        return 4


class Pentagon(Polygon):
    def no_of_sides(self):
        return 5


tri = Triangle()
print("Triangle has {} sides".format(tri.no_of_sides()))
# poly = Polygon()   # Error: TypeError: Can't instantiate abstract class Polygon with abstract methods no_of_sides
# print("Polygon has {} sides".format(poly.no_of_sides()))
