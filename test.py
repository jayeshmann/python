list1 = [1, "meow", "billi", 2, "cat", 3, "meows"]
print("only int", list(filter(lambda x: type(x) == int, list1)))
