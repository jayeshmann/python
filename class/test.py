class Cat:
    def __init__(self, breed='Persian'):
        self.breed = breed

    def getBreed(self):
        return self.breed


mew = Cat('Chartreux')

print(f"{mew.getBreed()} cat")
