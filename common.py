def get_decision_input(dec):
    while dec is not True:
        try:
            dec = int(input("Enter number: "))
            return dec
        except:
            pass