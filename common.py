import datetime
import random
import string
import data_manager

AMOUNT_INDEX = 1
CATEGORY_INDEX = 2
DETAILS_INDEX = 3
YEAR_INDEX = 4
MONTH_INDEX = 5
DAY_INDEX = 6

def sort(list_to_check):
    """ Function display options sort by date or sort by category"""

    running = True
    while running:
        try:
            sort_option = input("Do you want sort by date, category, value or detail [d/c/v/dt]:? ")

            if sort_option == "d":
                result_sort = sort_date(list_to_check)

            elif sort_option == "c":
                result_sort = sort_by_category(list_to_check)

            elif sort_option == "v":
                result_sort = sort_by_value(list_to_check)

            elif sort_option == "dt":
                result_sort = sort_by_detail(list_to_check)

            return result_sort

        except TypeError:
            print("Enter correct letter: ")

def sort_by_detail(list_to_check):
    """ Function return items category from list """

    detail_list = []

    get_item = input("What specific detail do you looking for?: ")
    for elements in list_to_check:
        if elements[DETAILS_INDEX] == get_item:
            detail_list.append(elements)

    return detail_list

def sort_by_value(list_to_check):
    """ Function return value category from list """

    amount_input = float(input("Enter amount to display above: "))
    sort_by_date = input("Do you want to display at specifc time [y/n]: ?")

    display_elements = []
    for elements in list_to_check:
        if float(elements[AMOUNT_INDEX]) >= amount_input:
            if sort_by_date == "n":
                display_elements.append(elements)
            elif sort_by_date == "y":
                data = sort_date(list_to_check)
                return data

    return display_elements

def sort_by_category(list_to_check):
    """ Function return category elements from list """

    display_elements = []

    get_category = input("Enter category: ")
    sort_by_date = input("Do you want to display at specifc time [y/n]: ?")

    for elements in list_to_check:
        if elements[CATEGORY_INDEX] == get_category:
            if sort_by_date == "n":
                display_elements.append(elements)
            elif sort_by_date == "y":
                data = sort_date(list_to_check)

                return data

    return display_elements

def sort_date(list_to_check):
    """ Function sort dates"""

    running = True
    while running:
        try:
            year_from, month_from, day_from, year_to, month_to, day_to = date_inputs()

            start = datetime.date(year_from, month_from, day_from)
            end = datetime.date(year_to, month_to, day_to)

            display_elements = []

            for elements in list_to_check:
                set_year = datetime.date(int(elements[YEAR_INDEX]), \
                int(elements[MONTH_INDEX]), int(elements[DAY_INDEX]))
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


def prepare_list_to_save(data):
    prepared = []
    for element in data:
        element = [element]
        prepared.append(element)
    return prepared
