import time
# Opening an existing text file
# Reading and printing all content at once
file = open("sample.txt", "r")
whole_content = file.read()
print(whole_content)

# Reseting the file pointer to initial position
# Reading each line and storing them in a list
file.seek(0)
lines = file.readlines()
for i, line in enumerate(lines):
    print(f"{i}th line - {line}")

# We will read the first four characters
file.seek(0)
print("Printing the first 4 characters.....")
time.sleep(2)
print(file.read(4))

file.close()