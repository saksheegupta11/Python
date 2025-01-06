# Write a program to swap the values of two variables using bitwise XOR operator.
a = int(input("Enter a :"))
b = int(input("Enter b :"))
a = a^b
b = a^b
a = a^b
print("a =",a)
print("b =",b)