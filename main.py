import display
import common
import income_expenses
import data_manager
from config import config
from raports import raport
import os
import intro
import time

def main():
    expenses = data_manager.data_import('expenses.txt')
    incomes = data_manager.data_import('earnings.txt')
    income_categories = income_expenses.get_category('income_categories.txt')
    expense_categories = income_expenses.get_category('categories.txt')

    os.system('clear')
    decision = 0


    while decision != 5:
        os.system('clear')
        display.print_message(intro.intro)
        display.print_message(intro.intro2)
        display.print_message("Main menu")
        menu = ['Expenses', 'Incomes', 'Raports', 'Categories configuration', 'Exit']  # main menu
        display.print_menu(menu)
        decision = common.get_decision_input(decision)
        os.system('clear')
        if decision == 1:
            income_expenses.expenses(expenses, expense_categories)
        elif decision == 2:
            income_expenses.incomes(incomes, income_categories)
        elif decision == 3:
            raport(incomes, expenses)
        elif decision == 4:
            config(income_categories, expense_categories)

    income_categories = common.prepare_list_to_save(income_categories)
    expense_categories = common.prepare_list_to_save(expense_categories)

    data_manager.data_export(expenses, 'expenses.txt')
    data_manager.data_export(incomes, 'earnings.txt')
    data_manager.data_export(income_categories, 'income_categories.txt')
    data_manager.data_export(expense_categories, 'categories.txt')


if __name__ == '__main__':
    main()
