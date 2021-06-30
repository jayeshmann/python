dict1 = {"cat": "neko", "dog": "inu"}

dog_popped = dict1.pop("dog")
print(type(dict1))
print("Dict after pop:", dict1)
print("Pop:", dog_popped)

dict1_str = str(dict1)
print(type(dict1_str))
