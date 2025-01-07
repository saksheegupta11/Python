# Write a program to check whether a number is even or odd using bitwise operator
a = int(input("Enter a number: "))

            # AND
if a & 1 == a:
    print(a, "is odd")       # a & 1 = 1
else:
    print(a,"is even")       # a & 1 = 0

            # OR    
if a | 1 == a:
    print(a, "is odd")       # a | 1 = a
else:
    print(a, "is even")      # a | 1 = a+1 
        
            # XOR
if a ^ 1 == a-1:
    print(a, "is odd")       # a ^ 1 = a-1
else:
    print(a, "is even")      # a ^ 1 = a+1
