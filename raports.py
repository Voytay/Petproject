import display
import common
import data_manager

def raport():
    decision = 0
    while decision != 4:
        display.print_message("Raports menu")
        menu = ['Generate raport', 'Show raports', 'Delete raports', 'Exit']
        display.print_menu(menu)
        decision = common.get_decision_input(decision)
        if decision == 1:
            gen_raport()
        elif decision == 2:
            show_list_raport()
        elif decision == 3:
            delete_raport()


def gen_raport():
    decision = 0
    while decision != 3:
        display.print_message("Generating raport")
        menu = ['Incomes', 'Expenses', 'Exit']
        display.print_menu(menu)
        decision = common.get_decision_input(decision)
        if decision == 1:
            data = data_manager.data_import('expenses.txt')
            prin = common.sort(data)
            display.print_data(prin, "header")
        elif decision == 2:
            data = data_manager.data_import('expenses.txt')
            common.sort(data)
