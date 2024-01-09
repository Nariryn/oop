def add2list(list1, list2):
    if len(list1) != len(list2):
        return print("ERROR")
    return [ list1[i] + list2[i] for i in range(len(list1))]

item1 = list(map(int, input("Enter first list of number: ").split()))
item2 = list(map(int, input ("Enter second list of number: ").split()))
print("Sum of lists:", add2list(item1, item2 ))