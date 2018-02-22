'''
Program configuration module
Allows to:
- change default categories of incomes and expenses

'''

import display
import common
import data_manager
import raports


def config():
    decision = 0
    while decision != 2:
        display.print_message("Config menu")
        menu = ['Categories', 'Exit']
        display.print_menu(menu)
        decision = common.get_decision_input(decision)
        if decision == 1:
            categories()


def categories():
    decision = 0
    while decision != 3:
        display.print_message("Config categories menu")
        menu = ['Show categories', 'Edit categories', 'Exit']
        display.print_menu(menu)
        decision = common.get_decision_input(decision)
        if decision == 1:
            cat = data_manager.data_import('categories.txt')
            display.print_list(cat, "Categories")
        elif decision == 2:
            edit_categories()


def edit_categories():
    decision = 0
    while decision != 3:
        display.print_message("Edit categories")
        menu = ['Add category', 'Delete category', 'Exit']
        display.print_menu(menu)
        decision = common.get_decision_input(decision)
        if decision == 1:
            add_category()
        elif decision == 2:
            remove_category()


def add_category():
    name = [input("Enter name of category: ")]
    cat = data_manager.data_import('categories.txt')
    cat.append(name)
    data_manager.data_export(cat, 'categories.txt')


def Magda_add_category(category):
    new_category = input('Enter new category: ')
    category.append(new_category)
    return category

def Magda_remove_category(category):
    removed_category = input('Enter name of category, which do you want remove: ')
    if removed_category in category:
        category.remove(removed_category)
    return category


def remove_category():
    name = input("Enter category to remove: ")
    cat = data_manager.data_import('categories.txt')
    for row in cat:
        for element in row:
            if element == name:
                to_remove = cat.index(row)
                cat.pop(to_remove)
    data_manager.data_export(cat, 'categories.txt')
