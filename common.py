import datetime
import random
import string
import data_manager


def sort(list_to_check):
    """ Function display options sort by date or sort by category"""

    category = 2
    year = 4
    month = 5
    day = 6



    sort_option = input("Do you want sort by date or category [d/c]?: ")
    if sort_option == "d":
        data = sort_date(list_to_check, year, month, day)
        return data

    elif sort_option == "c":
        display_elements = []

        get_category = input("Enter category: ")
        sort_by_date = input("Do you want to display at specifc time [y/n]: ?")
        for elements in list_to_check:
            if elements[category] == get_category:
                if sort_by_date == "n":
                    display_elements.append(elements)
                elif sort_by_date == "y":
                    sort_date(list_to_check, year, month, day)
        return display_elements

def sort_date(list_to_check, year, month, day):
    """ Function sort dates"""

    year_from = int(input("Give the year from [yyyy]: "))
    month_from = int(input("Give the month from [m]: "))
    day_from = int(input("Give the day from [d]: "))
    year_to = int(input("Give the year to [yyyy]: "))
    month_to = int(input("Give the month to [m]: "))
    day_to = int(input("Give the day to [d]: "))

    start = datetime.date(year_from,month_from,day_from)
    end = datetime.date(year_to,month_to,day_to)

    display_elements = []

    for elements in list_to_check:

        elements[year] = int(elements[year])
        elements[month] = int(elements[month])
        elements[day] = int(elements[day])
        set_year = datetime.date(elements[year],elements[month],elements[day])
        if set_year >= start and set_year <= end:
            display_elements.append(elements)

    return display_elements


def get_decision_input(dec):
    while dec is not True:
        try:
            dec = int(input("Enter number: "))
            return dec
        except:
            print("Not number!")


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
