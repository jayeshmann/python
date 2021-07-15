class Cat:

    __mostFamousBreed = 'Persian'

    def __init__(self, breed='Persian'):
        self.breed = breed

    def getBreed(self):
        return self.breed

    def getMostFamous(self):
        return Cat.__mostFamousBreed

    def setMostFamous(self, newFamous):
        Cat.__mostFamousBreed = newFamous


meow = Cat('Chartreux')

print(f"{meow.getBreed()} cat")
print(f"{meow.breed}")
print(f"{meow.__dict__}")
print(f"Most famous: {meow.getMostFamous()}")
try:
    print(f"{meow.__mostFamousBreed}")
except AttributeError:
    print("You tried to access private member")

meow.setMostFamous('British shorthair')

print(f"Most famous: {meow.getMostFamous()}")
