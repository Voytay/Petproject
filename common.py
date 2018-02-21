import datetime
import random
import string

def sort():

    myfile = [["xxx,xxx,shopp,xxx,2017,02,28"],["xxx,xxx,sx,xxx,2016,10,04"]]
    list_to_check = split_elements(myfile)
    category = 2
    year = 4
    month = 5
    day = 6

    sort_option = input("Do you want sort by date or category [d/c]?: ")

    if sort_option == "d":

        sort_date(list_to_check, year, month, day)



    elif sort_option == "c":
        get_category = input("Enter category: ") 
        sort_by_date = input("Do you want to display at specifc time [y/n]: ?")
        for elements in list_to_check:             
            if elements[category] == get_category:
                if sort_by_date == "n":
                    print(elements)

                elif sort_by_date == "y":
                    sort_date(list_to_check, year, month, day)
                    

def sort_date(list_to_check, year, month, day):

    year_from = int(input("Give the year from [yyyy]: "))
    month_from = int(input("Give the month from [m]: "))
    day_from = int(input("Give the day from [d]: "))
    year_to = int(input("Give the year to [yyyy]: "))
    month_to = int(input("Give the month to [m]: "))
    day_to = int(input("Give the day to [d]: "))


    start = datetime.date(year_from,month_from,day_from) 
    end = datetime.date(year_to,month_to,day_to)

    for elements in list_to_check:
        elements[year] = int(elements[year])
        elements[month] = int(elements[month])
        elements[day] = int(elements[day])
        set_year = datetime.date(elements[year],elements[month],elements[day])
        if set_year >= start and set_year <= end:
            print(elements)

    
def split_elements(myfile):
    
    list_to_check = []
    for elements in myfile:
        for i in elements:
            i = i.split(",")
            list_to_check.append(i)
    return list_to_check

sort()

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
