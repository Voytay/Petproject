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
            show_list_rap()
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
            data = data_manager.data_import('earnings.txt')
            common.sort(data)
        elif decision == 2:
            pass