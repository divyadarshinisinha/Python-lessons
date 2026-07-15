# Read names from words.txt
file = open("words.txt", "r")

names = []
for line in file:
    name = line.strip()      # Remove newline
    if len(name) > 4:
        names.append(name)

file.close()

# Write names to words_out.txt
out = open("words_out.txt", "w")

for name in names:
    out.write(name + "\n")

out.close()

print("Names with length greater than 4:")
for name in names:
    print(name)