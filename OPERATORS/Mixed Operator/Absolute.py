# Write a program to find the absolute value of a number without using built-in functions.
def absolute(a):
    if a < 0:
            return -a
    else:
        return a          

a = int(input("Enter a number :"))  
print(f"The absolute value of {a} is {absolute(a)}")        