data = list(map(int, input("Enter number: ").split()))
data.sort()
if data[0] == 0:
    data[0] = data[1]
    data[1] = 0

for i in range(len(data)):
    print(data[i], end='')