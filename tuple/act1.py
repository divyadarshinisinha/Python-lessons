# All about Tuple
# Create tuples "pasta" and "biryani"
pasta = ("Pasta Arrabiata", "Italian", 20, "Medium")
biryani = ("Chicken Biryani", "Indian", 45, "Hard")

# Display values
print("Recipe 1 : ", pasta)
print("Name of Recipe 1 : ", pasta[0])
print("Cuisine of Recipe 1 : ", pasta[1])
print(f"Prep Time of Recipe 1 :{pasta[2]} minutes")
print("Difficulty level of Recipe 1 : ", pasta[-1])

print("\n")
print("*"*30)
print("\n")

# tuple slicing 
# combine two tuples ==> nested tuple
all_tuples = (pasta, biryani)
print(f"First Recipe Name : {all_tuples[0][0]}")
print(f"Second Recipe Name : {all_tuples[1][0]}")
print(f"Second Recipe Prep Time : {all_tuples[1][2]} mins")
print(f"Second Recipe Difficulty level : {all_tuples[1][3]}")

print("\n")
print("*"*30)
print("\n")

#iterate through a tuple
print("Iterate/Loop through a Tuple")
for detail in pasta:
    print("-", detail)

print("\n")
print("*"*30)
print("\n")

#Enumerate
print("Enumerate through a Tuple")
for idx, detail in enumerate(biryani, start=1):
    print(f"{idx} : {detail}")

#Tuple Unpacking
print("\n Tuple Unpacking")
print("*"*30)
print("\n")

fruits = ("apple", "banana", "kiwi", "orange", "guava")
f1, f2, f3, f4, f5 = fruits
print(f1)
print(f2)
print(f3)
print(f4)

#Advanced tuple unpacking
x , *y = fruits
print(x)
print(y)

#index()
print(fruits.index("apple"))

#count()
print(fruits.count("apple"))

#in
print("apple" in fruits)
print("apple" not in fruits)

#Zip
t1 = (1,2,3)
t2 = ("John", "David", "Mayank")

t3 = dict(zip(t1,t2))

print("\n")
print("*"*30)
print("\n")
for id, name in t3.items():
    print(f"{id} : {name}")
    