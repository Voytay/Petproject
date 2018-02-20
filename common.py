import random
import string

def get_decision_input(dec):
    while dec is not True:
        try:
            dec = int(input("Enter number: "))
            return dec
        except:
            pass


def generate_id(data):
    sign = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "+"]  
    unique = False
    while unique == False:
        ids = "".join([random.choice(string.ascii_lowercase), 
                    random.choice(sign),
                    random.choice(string.digits),
                    random.choice(string.ascii_uppercase)])
        unique = True
        
        ids_index = 0
        for row in data:
            if row[ids_index] == ids:
                unique = False
    return ids