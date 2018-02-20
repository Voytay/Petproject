'''
Program configuration module
Allows to:
- change default categories of incomes and expenses



'''

import display
import common
import data_manager

def config():
    while True:
        display.print_message("Config menu")
        menu = ['Categories', ' Raports', 'Exit']
        display.print_menu(menu)
        dec = 0
        dec = common.get_decision_input(dec)
        if dec == 1:
            categories()
        if dec == 2:
            pass
        if dec == 3:
            return False


def categories():
    while True:
        dec = 0
        display.print_message("Categories menu")
        menu = ['Show categories', 'Edit categories']
        display.print_menu(menu)
        dec = common.get_decision_input(dec)
        if dec == 1:
            cat = data_manager.data_import('categories.txt')
            display.print_data(cat, 'Categories')
        if dec == 2:
            pass
        if dec == 3:
            return False