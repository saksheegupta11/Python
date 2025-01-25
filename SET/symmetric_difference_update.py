# Write a program to update a set with the symmetric difference of itself and another set.
s1 = {1,2,3,4,5}
s2 = {9,8,7,6,5,4,3,2,1}
print("s1 before symmetric difference update: ",s1)
print("s2 before symmetric difference update: ",s2)
s1.symmetric_difference_update(s2)
print("s1 after symmetric difference update: ",s1)

# after s1 updated with symmetric difference of s2
s2.symmetric_difference_update(s1)
print("s2 after symmetric difference update: ",s2)