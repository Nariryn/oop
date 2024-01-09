def is_plusone_dictionary(dic):
    dic_arr = []
    for key, value in dic.items():
        dic_arr.append(key)
        dic_arr.append(value)
    return dic_arr == sorted(dic_arr) and dic_arr == list(range(min(dic_arr), max(dic_arr) + 1))

# Example usage:
dictionary1 = {1: 2, 3: 4, 5: 6, 7: 8}
print(is_plusone_dictionary(dictionary1))  # Output: True

dictionary2 = {1: 2, 3: 10, 5: 6, 7: 8}
print(is_plusone_dictionary(dictionary2))  # Output: False
