#dictionary
d = {1: "Python", '2': "Java", "name": "C++", 'd2': {6: "I", 5: "J"}}

#how to print whole dictionary
print(d)

#printing specific things from the dictionary
print(d[1])
print(d['2'])
print(d['name'])

#dictionary manipulation
d1 = {0: "A", 5: "B"}
d_new = d
d_new.update(d1)
print(d_new)

#tuple
t = (1,2,3,4,5,6)
print(t)

#empty tuple
t_empty = ()

#set
s = {1,2,3,4,5,6}
print(s)

#set with duplicate values, but it will auto remove those values
s1 = {1,2,3,3,4,5,6}
print(s1)

#how to declare empty set
s_empty = set()

#set union and intersection
s2 = {1, 2, 3, 4, 5}
s3 = {4, 5, 6, 7, 8}

#union - combines all elements from both sets
union_result = s2 | s3
print("Union:", union_result)

#intersection - common elements from both sets
intersection_result = s2 & s3
print("Intersection:", intersection_result)