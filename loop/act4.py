# Calculate Sum of n natural numbers
limit = int(input("Enter limit : "))
start = 1
total = 0
while start <= limit:
    total += start
    start += 1

print(f"Sum upto {limit} is : {total}")