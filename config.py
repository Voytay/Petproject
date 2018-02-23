'''
Program configuration module
Allows to:
- change default categories of incomes and expenses

'''

import display
import common
import data_manager
import raports


def config(cat_income, cat_expenses):
    decision = 0
    while decision != 3:
        display.print_message("Configuration menu")
        menu = ['Incomes', 'Expenses', 'Back to main menu']
        display.print_menu(menu)
        decision = common.get_decision_input(decision)
        if decision == 1:
            cat_income = what_to_do(cat_income)
        elif decision == 2:
            cat_expenses = what_to_do(cat_expenses)
    return cat_income, cat_expenses


def what_to_do(category):
    decision = 0
    table = []
    while decision != 4:
        display.print_message("What you want to do?")
        menu = ['Show categories', 'Add category', 'Remove category', 'Back to configuration menu']
        display.print_menu(menu)
        decision = common.get_decision_input(decision)
        if decision == 1:
            for element in category:
                print(element)
        elif decision == 2:
            category = add_category(category)
        elif decision == 3:
            category = remove_category(category)
    return category


def edit_category():
    decision = 0
    while decision != 3:
        display.print_message("Edit categories")
        menu = ['Add category', 'Delete category', 'Return ']
        display.print_menu(menu)
        decision = common.get_decision_input(decision)
        if decision == 1:
            add_category()
        elif decision == 2:
            remove_category()


def add_category(category):
    new_category = input('Enter new category: ')
    category.append(new_category)
    return category


def remove_category(category):
    removed_category = input('Enter name of category, which do you want remove: ')
    if removed_category in category:
        category.remove(removed_category)
    return category


