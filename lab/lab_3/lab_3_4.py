def char_count(str):
    result_dict = {}
    for char in str:
        result_dict[char] = result_dict.get(char, 0) + 1
    return result_dict

input_string = input("Enter string: ")
result = char_count(input_string)
print(result)
