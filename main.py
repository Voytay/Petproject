import display
import common
import income_expenses
import data_manager
from config import config
from raports import raport
import os
import intro

def main():
    os.system('clear')
    decision = 0

    display.print_message(intro.intro)
    display.print_message(intro.intro2)
    while decision != 5:
        display.print_message("Main menu")
        menu = ['Expenses', 'Incomes', 'Raports', '###Config', 'Exit'] # main menu
        display.print_menu(menu)
        decision = common.get_decision_input(decision)
        os.system('clear')
        if decision == 1:
            #income_expenses.xxx
            pass
        elif decision == 2:
            #income_expenses.yyy
            pass
        elif decision == 3:
            raport()
        elif decision == 4:
            config()
        else:
            display.print_message("No option!")


if __name__ == '__main__':
    main()