# Bubble Sort

input_list = [9, 4, 7, 2, 1, 0, 5, 7]

print(input_list)

for i in range(input_list.__len__()):
    for j in range(len(input_list) - i - 1):
        if input_list[j] > input_list[j+1]:
            input_list[j], input_list[j+1] = input_list[j+1], input_list[j]

print(input_list)
