import datetime
import random
import string
import data_manager


def sort(list_to_check):
    """ Function display options sort by date or sort by category"""
    value = 1
    category = 2
    item = 3
    year = 4
    month = 5
    day = 6
    

    running = True
    while running:
        try:
            sort_option = input("Do you want sort by date, category, value or item ?[d/c/v/i]?: ")

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
                            data = sort_date(list_to_check, year, month, day)

                            return data

                return display_elements

            elif sort_option == "v":
                sort_by_date = input("Do you want to display at specifc time [y/n]: ?")
                display_elements = []
                for elements in list_to_check:
                    if sort_by_date == "n":
                        display_elements.append(elements)
                    elif sort_by_date == "y":
                        data = sort_date(list_to_check, year, month, day)
                        return data

                return display_elements    

            elif sort_option == "i":
                item_list = []

                get_item = input("What kind of item do you looking for?: ")
                for elements in list_to_check:
                    if elements[item] == get_item:
                        item_list.append(elements)
                        
                return item_list
                        
                    


        except TypeError:
            print("Enter correct letter: ")

def sort_date(list_to_check, year, month, day):
    """ Function sort dates"""

    running = True
    while running:
        try:
            year_from, month_from, day_from, year_to, month_to, day_to = date_inputs()

            start = datetime.date(year_from, month_from, day_from)
            end = datetime.date(year_to, month_to, day_to)

            display_elements = []

            for elements in list_to_check:
                set_year = datetime.date(int(elements[year]), \
                int(elements[month]), int(elements[day]))
                if set_year >= start and set_year <= end:
                    display_elements.append(elements)
                    running = False
            return display_elements

        except ValueError:
            print("Enter correct number: ")

def date_inputs():
    """ Function take inputs from user """

    year_from = int(input("Give the year from [yyyy]: "))
    month_from = int(input("Give the month from [m]: "))
    day_from = int(input("Give the day from [d]: "))
    year_to = int(input("Give the year to [yyyy]: "))
    month_to = int(input("Give the month to [m]: "))
    day_to = int(input("Give the day to [d]: "))

    return year_from, month_from, day_from, year_to, month_to, day_to


def get_decision_input(dec, prompt="Enter number: "):
    while dec is not True:
        try:
            dec = int(input(prompt))
            return dec
        except:
            print("Not number!")


def generate_id(data):
    sign = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "+"]
    unique = False
    while unique is False:
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
