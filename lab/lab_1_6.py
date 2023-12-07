'''
n = 10

for row in range(n):
    for col in range(n):
        if row + col < n:
            print(" ", end="")
        else:
            print("#", end ="")
    print("#")
'''
n = 10
for i in range(1,n):
    print(" "*(n-i),"#" * i)