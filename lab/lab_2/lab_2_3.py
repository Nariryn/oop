def delete_minus(data):
    return [[num for num in sublist if num >= 0]for sublist in data]
#    return [[num for num in sublist if num >= 0] for sublist in x]

data = [[1,1,1],[-3,2,4],[-5,5,-5]]
#input_data = list(map(int, input("Enter number: ").split()))
result = delete_minus(data)
print("Answer:", result)