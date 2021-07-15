class Football:
    def __init__(self, country, division, no_of_times) -> None:
        self.country = country
        self.division = division
        self.no_of_times = no_of_times

    def fifa(self):
        print(f"{self.country} team is placed in '{self.division}' FIFA division.")


class WorldChampions(Football):
    def __init__(self, country="Germany", division="UEFA", no_of_times=4) -> None:
        super().__init__(country, division, no_of_times)

    def world_championship(self):
        print(f"{self.country} team is {self.no_of_times} times world champions.")


germany = WorldChampions("Germany", "UEFA", 4)
germany.fifa()
germany.world_championship()
