import display
import common


def main():
    menu = ['Expenses', 'Incomes', 'Raports']
    display.print_menu(menu)
    dec = common.get_input()
    if dec == 1:
        #expenses module
        pass
    elif dec == 2:
        # Incomes module
        pass
    elif dec == 3:
        # raport module
        pass


if __name__ == '__main__':
    main()