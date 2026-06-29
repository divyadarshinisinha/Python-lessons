# Recursion
def recursiveFn(n):
    if n == 0 or n == 1:
        return 1
    return n * recursiveFn(n - 1)

while True:
    try:
        user_input = input("Enter a number to find its factorial (or type 'no' to quit): ")
        if user_input.lower() in ['no', 'n', 'stop']:
            break
        num = int(user_input)
        if num < 0:
            print("Enter a valid input")
            continue
        print(recursiveFn(num))
    except ValueError:
        print("Enter only numbers...")
        continue
    answer = input("Do you want to continue? (yes/no): ").lower()
    if answer not in ['yes', 'y']:
        break
print("Factorial ends...")