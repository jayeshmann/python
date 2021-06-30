test_dict = {"Gfg": 2, "is": 1, "Best": 3}

print("Orig dict:", test_dict)

dict_list = [{"for": 3, 'all': 7}, {'geeks': 10}, {'and': 1, 'CS': 9}]

for dicts in dict_list:
    test_dict.update(dicts)

print("updated:", test_dict)
