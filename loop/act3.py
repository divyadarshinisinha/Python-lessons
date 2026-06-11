n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    # Print leading spaces to center the triangle
    print(' ' * (n - i), end='')
    
    # Print the stars with a space in between
    for j in range(i):
        print('*', end=' ')
    print()