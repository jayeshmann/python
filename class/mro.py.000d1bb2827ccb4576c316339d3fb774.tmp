class A:
	def my_method(self):
		print("A")

class C:
	def my_method(self):
		print("C")

class B:
	def my_method(self):
		print("B")


class X(A,B):
	def my_method(self):
		print("X")


class Y(B,C):
	def my_method(self):
		print("Y")


class P(X, Y):
	pass


obj = P()
obj.my_method()
print(P.mro())
