# skip lines
word = input("Enter lines starting with : ")
file = open("sample.txt", "r")

lines = file.readlines()
for line in lines:
    if linestartswith(word):
        continue
    else:
        print(line.strip())
file.close()