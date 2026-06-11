# Number Table
print("This is a Number Table")
print("*"*30)

num = int(input("Enter a number : "))

for i in range(1,11):
    print(f"{num} X {i} : {num * i}")