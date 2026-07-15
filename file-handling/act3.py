file = open('sample.txt','r')
lines = file.readlines()
file.close()

outFile = open('odd_lines.txt',"w")

for i in range(0, len(lines),2):
    outFile.write(lines[i])

outFile.close()
print("Odd lines are saved in outFile.txt")