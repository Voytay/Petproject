import display
import common
import data_manager
import os


def raport(income, expenses):
    decision = 0
    while decision != 5:
        display.print_message("Raports menu")
        menu = ['Generate raport', 'Show raports', 'Show specified raport', 'Delete raports', 'Back to main menu']
        display.print_menu(menu)
        decision = common.get_decision_input(decision)
        if decision == 1:
            gen_raport(income, expenses)
        elif decision == 2:
            data = get_list_raport()
            display.print_list(data, 'Files: \n')
        elif decision == 3:
            data = get_list_raport()
            filename = validate_filename(data)
            show_raport(filename)
        elif decision == 4:
            data = get_list_raport()
            filename = validate_filename(data)
            delete_raport(filename)


def gen_raport(income, expenses):
    decision = 0
    while decision != 3:
        display.print_message("Generating raport menu")
        menu = ['Incomes', 'Expenses', 'Back to raports menu']
        display.print_menu(menu)
        decision = common.get_decision_input(decision)

        if decision == 1:
            data = common.sort(income)
            display.print_table(data)
            save_raport(data)
        elif decision == 2:
            data = common.sort(expenses)
            display.print_table(data)
            save_raport(data)


def save_raport(data):
    if_want_save = 0
    display.print_message("Do you want to save this raport? Press 1 to save: ")
    if_want_save = common.get_decision_input(if_want_save)
    if if_want_save == 1:
        filename = input("Enter filename: ")
        data_manager.data_export(data, filename+"_raport.txt")


def get_list_raport():
    table = []
    for file in os.listdir("./"):
        if file.endswith("_raport.txt"):
            table.append(file)
    return table


def validate_filename(list_of_files):
    filename = input("Enter filename: ")
    for element in list_of_files:
        if element == filename:
            return filename


def delete_raport(filename):
    if filename:
        os.remove(filename)
        display.print_message("Raport " + filename + " removed!")
    else:
        display.print_message("No such file!")


def show_raport(filename):
    if filename:
        data = data_manager.data_import(filename)
        display.print_table(data)
    else:
        display.print_message("No such file!")

