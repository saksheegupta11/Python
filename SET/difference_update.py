# Write a propgram to update the difference between two sets.
s1 = {23,45,83,909,113,1347,8452}
s2 = {2354,735,2435,5,23,367,45,9673,657,8364,8452}
print("s1 before difference update: ",s1)
print("s2 before difference update: ",s2)
s1.difference_update(s2)
print("s1 difference update with s2: ",s1)
