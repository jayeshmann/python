alphabet = "google"

index = 0
print(f"In the string '{alphabet}'")
for each_character in alphabet:
    print(f"Character '{each_character}' has an index value of {index}")
    index += 1

a = alphabet.__iter__()

print(a.__next__())
