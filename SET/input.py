# Write a program to take input in set
A = set()
num = int(input("Enter the number of elements you want to store: "))
print("Enter the elements: ")
for x in range(num):
    value = input()
    A.add(value)
print(A)    