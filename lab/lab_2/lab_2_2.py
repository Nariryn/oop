def count_char_in_string(words, char):
  return [word.count(char) for word in words]

list_x = input("Enter words: ").split()
char_c = input("Enter char: ")
result = count_char_in_string(list_x, char_c )
print("Answer:", result)