def printFullname(first_name, last_name, greet = "Hi"):
    return f"{greet}, {first_name} {last_name}"

while True:
    fname = input("Enter your first name : ")
    lname = input("Enter your last name : ")
    greet = input("Enter greeting : ")

    if greet == "":
        print(printFullname(fname, lname))
    else:
        print(printFullname(fname, lname, greet))
        
    print("Do you want to continue?")
    answer = input("yes/no ? : ")

    if answer not in ['yes', 'y']:
        exit()