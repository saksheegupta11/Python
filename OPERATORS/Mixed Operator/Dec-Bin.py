#  Write a program to convert a decimal number to binary using bitwise operators.
a = int(input("Enter a number :"))  
b = a
c = 0
d = 1
while a > 0:
    c = c+(a%2)*d
    d*=10
    a = a//2
print("The binary equivalent of",b,"is",c)  
