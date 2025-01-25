# Write a propgram to update a set with the intersection of itself and another set.
s1 = {1,2,3,4,5}
s2 = {9,8,7,6,5,4,3,2,1}
print("s1 before intersection update: ",s1)
print("s2 before intersection update: ",s2)
s1.intersection_update(s2)
print("s1 after intersection update: ",s1)
