#Write a program to check if a set is a subset of another set.
s1 = {"Swapnil", "Sakshee", "Radhe", "Shalendra"}
s2 = {"Rakesh", "Prachi", "Shanu", "Sakshee", "Swapnil", "Radhe", "Shalendra"}
print("s1 is subset of s2: ",s1.issubset(s2))
print("s2 is subset of s1: ",s2.issubset(s1))