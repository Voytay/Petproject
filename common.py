def get_input():
    try:
        dec = int(input("Enter number: "))
        return dec
    except ValueError:
        print("Wrong key!")
        get_input()