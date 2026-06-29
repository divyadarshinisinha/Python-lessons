# All about list in python

myList = []
print("Empty list : ", myList)

myList2 = [11,4,7,99,3,12]
print(myList2)

# Access the first item form myList2
print(myList2[0])

# Access the last item from myList2
print(myList2[-1])


# slice
print(myList2[1:3])


# List Methods
print("My list : ", myList2)

#append()
myList2.append(33)
print(myList2)

# remove
myList2.remove(99)
print(myList2)


# pop()
myList2.pop()
print(myList2)

myList2.pop(2)
print(myList2)

# sort
print("Current list : ", myList2)
myList2.sort()
print("After sorting : ", myList2)

# reverse

# method 1
myList2.reverse()
print(myList2)

# method 2