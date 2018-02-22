import data_manager
import display
import common as c
from datetime import date


def get_category(filename):
    CATEGORY_INDEX = 0
    category_list = []
    category = data_manager.data_import(filename)

    for element in category:
        category_list.append(element[CATEGORY_INDEX])
    return category_list


def expenses(expenses, expense_categories):
    expense_options = ['Add expense', 'Remove expense', 'Edit expense', \
    'Display expenses in the current month', 'Back to main menu']
    selected_option = 0

    while selected_option != '5':
        try:
            display.print_menu(expense_options)
            selected_option = input('Enter a number: ')

            if selected_option == '1':
                add_record(expense_categories, expenses)
            elif selected_option == '2':
                remove_record(expenses)
            elif selected_option == '3':
                edit_record(expenses, expense_categories)
            elif selected_option == '4':
                display_current_month(expenses)

        except ValueError:
            print('Wrong value. Please, try again.')
        except IndexError:
            print('Wrong number. Please, try again. ')


def sum_amount(data):
    sum_amount = 0

    for element in data:
        element[c.AMOUNT_INDEX] = float(element[c.AMOUNT_INDEX])
        sum_amount += element[c.AMOUNT_INDEX]
    return str(sum_amount)


def add_record(category, data_):
    YEAR_INDEX = 0
    MONTH_INDEX = 1
    DAY_INDEX = 2
    record = [c.generate_id(data_)]

    amount = float(input('Enter the amount [0.0]: '))
    amount = format(amount, '.2f')
    record.append(str(amount))

    display.print_menu(category)
    selected_category = int(input('Chose category number: '))
    record.append(category[selected_category-1])

    operation_details = input('Enter the operation details: ')
    record.append(operation_details)

    expanse_date = date.today()
    expanse_date = expanse_date.timetuple()
    record.append(str(expanse_date[YEAR_INDEX]))
    record.append(str(expanse_date[MONTH_INDEX]))
    record.append(str(expanse_date[DAY_INDEX]))

    data_.append(record)
    print('Record added correctly. \n')
    return data_


def remove_record(data):
    display.print_table(data)
    removed_record = input('Enter id of record, which do you want remove: ')

    for element in data[:]:
        if removed_record == element[c.ID_INDEX]:
            data.remove(element)
    return data


def edit_record(data, category):
    options = ['Amount', 'Categories', 'Details', 'Year', 'Month', 'Day']

    display.print_table(data)
    edited_record = input('Enter id of record, which do you want edit: ')
    for element in data[:]:
        if edited_record == element[c.ID_INDEX]:
            display.print_menu(options)
            selected_option = int(input('Enter number, which element do you want edit: '))

            if selected_option == 1:
                new_amount = format(float(input('Enter the amount [0.0]: ')), '.2f')
                element[selected_option] = str(new_amount)
            elif selected_option == 2:
                display.print_menu(category)
                selected_category = int(input('Chose category number: '))
                element[selected_option] = category[selected_category-1]
            elif selected_option == 3:
                new_details = input('Enter new details: ')
                element[selected_option] = new_details
            elif selected_option in (4, 5, 6):
                new_date = int(input('Enter new date: '))
                element[selected_option] = new_details

    return data


def display_current_month(data):
    MONTH_INDEX = 1
    current_month_list = []

    current_date= date.today()
    current_date = current_date.timetuple()
    current_month = str(current_date[MONTH_INDEX])

    for element in data:
        if element[c.MONTH_INDEX] == current_month:
            current_month_list.append(element)
    if current_month_list == []:
        print('No record to display.')
    else:
        display.print_table(current_month_list)
        sum_amount_ = sum_amount(current_month_list)
        print('Sum: ' + sum_amount_ + ' EUR\n')


def incomes(incomes, income_categories):
    income_options = ['Add income', 'Remove income', 'Edit income', 'Display incomes in the current month',\
    'Back to main menu']
    selected_option = 0

    while selected_option != '5':
        try:
            display.print_menu(income_options)
            selected_option = input('Enter a number: ')

            if selected_option == '1':
                add_record(income_categories, incomes)
            elif selected_option == '2':
                remove_record(incomes)
            elif selected_option == '3':
                edit_record(incomes, income_categories)
            elif selected_option == '4':
                display_current_month(incomes)
        except ValueError:
            print('Wrong value. Please, try again.')
        except IndexError:
            print('Wrong number. Please, try again. ')
