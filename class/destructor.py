class Sample:
    num = 0

    def __init__(self, x):
        Sample.num += 1
        self.x = x
        print("x=", x)

    def __del__(self):
        Sample.num -= 1
        print("object value:", self.x, "exited from scope")


S1 = Sample(15)
S2 = Sample(35)
S3 = Sample(45)
