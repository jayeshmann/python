class Poissonier:
    def __init__(self, poissonier_role):
        self.poissonier_role = poissonier_role

    def display_poissonier_chef_info(self):
        print("Poissonier chef is a {}".format(self.poissonier_role))


class Entremetier:
    def __init__(self, entremetier_role):
        self.entremetier_role = entremetier_role

    def display_entremetier_chef_info(self):
        print("Entremetier chef is a {}".format(self.entremetier_role))


class Cook(Poissonier, Entremetier):
    def __init__(self, poissonier_role, entremetier_role):
        Poissonier.__init__(self, poissonier_role)
        Entremetier.__init__(self, entremetier_role)

    def display_cook_chef_info(self):
        self.display_poissonier_chef_info()
        self.display_entremetier_chef_info()


if __name__ == "__main__":
    print("issubclass: ", issubclass(Cook, (Poissonier, Entremetier)))
    cook = Cook("Seafood Chef", "Vegetables Chef")
    cook.display_cook_chef_info()
