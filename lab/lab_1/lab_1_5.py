large_palindrome = 0

def is_palindrome(number):
    return str(number) == str(number)[::-1]

for i in range(100, 999):
    for j in range(i, 999):
        sum = i * j
        if is_palindrome(sum) and sum > large_palindrome:
            large_palindrome = sum

print(large_palindrome)
