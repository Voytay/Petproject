import display
import common
import income_expenses

def main():
    menu = ['Expenses', 'Incomes', 'Raports', '###Config'] # main menu
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
        # config module
        pass
    else:
        print("Wrong key!!!!")

if __name__ == '__main__':
    main()