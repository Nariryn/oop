
input_string = input("Enter a string: ")

lower_count = 0
upper_count = 0

for char in input_string:
    if char.islower():
        lower_count += 1
    if char.isupper():
        upper_count += 1

print(lower_count)
print(upper_count)
