import display
import common
import income_expenses
import data_manager
from config import config
from raports import raport

def main():
    decision = 0
    while decision != 5:
        menu = ['Expenses', 'Incomes', 'Raports', '###Config', 'Exit'] # main menu
        display.print_menu(menu)
        #data = [['1','2000','data','kategoria']]
        data = data_manager.data_import('expenses.txt')
        decision = common.get_decision_input(decision)
        header = ['L.p', 'Kwota','kategoria','opis','data']
        #display.print_data(data, header)
        #header = 'HEADER----------------H'
        display.print_data(data, header)
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