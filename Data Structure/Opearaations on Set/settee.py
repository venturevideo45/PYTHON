my_set = {1, 2 , 2, 3, 4, 4, 4}
print("My Set :", my_set)

my_set.add(5)
print("Updated Set :", my_set)

set1 = my_set
set2 = {4, 4, 5, 6, 6, 7, 7, 7}
print("Set 1 :", set1)
print("Set 2 :", set2)
print("Union of Set 1 and Set 2 :", set1.union(set2))
print("Intersection of Set 1 and Set 2 :", set1.intersection(set2))
print("Difference of Set 1 and Set 2 :", set1.difference(set2))
print("Symmetric Difference of Set 1 and Set 2 :", set1.symmetric_difference(set2))