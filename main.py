import display
import common
import income_expenses
from config import config

def main():
    while True:
        menu = ['Expenses', 'Incomes', 'Raports', '###Config', 'Exit'] # main menu
        display.print_menu(menu)
        dec = 0
        dec = common.get_decision_input(dec)
        #header = 'HEADER----------------H'
        #data = [['1','2000','data','kategoria']]
        #display.print_data(data, header)
        if dec == 1:
            #income_expenses.xxx
            pass
        elif dec == 2:
            #income_expenses.yyy
            pass
        elif dec == 3:
            # raport module
            pass
        elif dec == 4:
            config()
        elif dec == 5:
            return False
        else:
            display.print_message("No option!")

if __name__ == '__main__':
    main()