#All about set

#create a set
prime_numbers = {2,3,5,5,7,7}
print(prime_numbers)

#copying set
#Shallow copy
prime_copy = prime_numbers.copy()
print(f"Original Set : {prime_numbers}")
print(f"Copied Set : {prime_copy}")

# Equality
print(prime_numbers == prime_copy)
print(prime_numbers is prime_copy)

#Adding
prime_numbers.add(11)
prime_numbers.add(7)
print(f"After adding new elements : {prime_numbers}")

#Remove
# 1. Discard : Safe removal
prime_numbers.discard(7)
prime_numbers.discard(10)
print(f"After removal : {prime_numbers}")

# 2. Remove : Raise Exception
item_to_remove = 100
try:
    print("Trying to remove '100'form SET...")
    prime_numbers.remove(100)
    print("Successfully removed")
except KeyError:
    print(f"{item_to_remove} not found.....")
finally:
    print("Program ends.....")

try:
    print("Trying to remove '5' form SET...")
    prime_numbers.remove(5)
    print("Successfully removed")
except KeyError:
    print(f"{item_to_remove} not found.....")
finally:
    print("Program ends")

# 3. pop()
popped_val = prime_numbers.pop()
print(f"item removed : {popped_val}")
print(f"After Item Removed : {prime_numbers}")

set1 = {1,2,3,4}
set2 = {3,4,5,6}

#union
print(set1.union(set2))

#intersection
print(set1.intersection(set2))

#diff
print(set1.difference(set2))
print(set2.difference(set1))

#Symetric Diff
print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))

#issubset, issuperset, disjoint
print({1,2}.issubset(set1))
print({1,2,3,4,5,6}.issuperset(set1))
print({1,2}.isdisjoint({3,4}))

#clear
set1.clear()

#del
del set1
print(set1)