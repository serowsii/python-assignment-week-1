#create an empty list
my_list = []

#append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#insert a value to the second position
my_list.insert(1, 15)

#extend the list
my_list.extend([50, 60, 70])

#remove the last element (add the last element here its 70)
#my_list.pop(70)
my_list.pop()

#sort the list in ascending order
my_list.sort()

#lets find and print the index of the value 30 from the list
index_of_30 = my_list.index(30)

print("Index of 30:", index_of_30)
print(my_list)
