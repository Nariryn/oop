def count_minus(input_str):
    numbers = [int(x) for x in input_str]
    count = sum([1 for num in numbers if num < 0])

    return count

input_data = input("Enter number: ").split()
result = count_minus(input_data)
print("Answer:", result)
