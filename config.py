'''
Program configuration module
Allows to:
- change default categories of incomes and expenses

'''

import display
import common
import data_manager


def config():
    decision = 0
    while decision != 3:
        display.print_message("Config menu")
        menu = ['Categories', ' Raports', 'Exit']
        display.print_menu(menu)
        decision = common.get_decision_input(decision)
        if decision == 1:
            categories()
        elif decision == 2:
            pass


def categories():
    decision = 0
    while decision != 3:
        decision = 0
        display.print_message("Categories menu")
        menu = ['Show categories', 'Edit categories', 'Exit']
        display.print_menu(menu)
        decision = common.get_decision_input(decision)
        if decision == 1:
            cat = data_manager.data_import('categories.txt')
            display.print_message(cat)
        elif decision == 2:
            pass