def only_english(string):
  return "".join([char for char in string if char.isalpha()])

input_data = input("Enter string: ")
result = only_english(input_data)
print("Answer:", result)