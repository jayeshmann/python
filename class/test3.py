class Country:
    def __init__(self, country_name) -> None:
        self.country_name = country_name

    def country_details(self) -> None:
        print(f"This country in the world is called {self.country_name}")


class HappiestCountry(Country):
    def __init__(self, country_name, continent) -> None:
        super().__init__(country_name)
        self.continent = continent

    def country_details(self) -> None:
        print(
            f"Happiest Country in the world is {self.country_name} and is in {self.continent}")


if __name__ == "__main__":
    finland = HappiestCountry("Finland", "Europe")
    finland.country_details()
