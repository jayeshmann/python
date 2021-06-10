len_of_l = int(input("list size> "))

p_sum, n_sum = 0, 0
l = [int(input(f"Element {i+1}>> "))
     for i in range(len_of_l)]

for item in l:
    if item > 0:
        p_sum += item
    else:
        n_sum += item

avg = (p_sum+n_sum)//len_of_l

above_avg = [item for item in l if item > avg]

print("Sum of positive elements:", p_sum)
print("Sum of negative elements:", n_sum)
print("Average:", avg)
print("Elements above average:", end=" ")
print(*above_avg, sep=', ')
