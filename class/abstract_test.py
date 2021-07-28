from abc import ABC, abstractmethod


class R(ABC):
    def rk(self):
        print("Abstract Base Class")


class K(R):
    def rk(self):
        super().rk()
        print("Sub Class")


r = K()
r.rk()

obj = R()
obj.rk()
