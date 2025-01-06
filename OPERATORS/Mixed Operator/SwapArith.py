# Write a program to swap the values of two variables using arithmetic operators.
a = int(input("Enter a: "))
b = int(input("Enter b: "))

# Swapping using 3rd variable
print("Using 3rd variable")
c = a
a = a + b - a
print("The value of a is:", a)
b = b + c - b
print("The value of b is:", b)

print("Without using 3rd variable")

# Swapping without using 3rd variable
x = int(input("Enter x: "))
y = int(input("Enter y: "))
x = x + y
y = x - y
x = x - y
print("The value of x is:", x)
print("The value of y is:", y)