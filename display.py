import data_manager
def print_menu(data):
    i = 1
    for element in data:
        print(i, "----->", element.title())
        i += 1


def print_data(data, header):

    print("|{:^4}|{:^6}|{:^10}|{:^30}|{:^12}|".format(*header))

    for element in data:
        print("|{:<4}|{:^6}|{:^10}|{:^30}|{:^12}|".format(*element))


def print_message(message):
    print(message)


def print_table(data, title):
    lenght = [6, 8, 15, 30, 6, 4, 4]
    additional_characters = 16
    width = sum(lenght) + additional_characters
    row = []

    for i in range(len(title)):
        row.append("| " + title[i].center(lenght[i]))
    row.append(" |")
    print("".join(row))
    print("="*width)

    for item in data:
        row = []
        for i in range(len(title)):
            row.append("| " + item[i].rjust(lenght[i]))
        row.append(" |")
        print("".join(row))


def get_longest(param):
    data = data_manager.data_import('expenses.txt')
    maxx = 0
    for element in data:
        if len(element[param]) > maxx:
            maxx = len(element[param])
    return maxx

def total(filename):
    total = 0
    data = data_manager.data_import(filename)
    for element in data:
        total += float(element[1])
    return str(total)

def print_percentage_spent():
    spent = total('expenses.txt')
    totalz = total('earnings.txt')
    print_message("Total spent: " + spent + ' of ' + totalz + " | Left: {:.2%}".format((float(totalz)-float(spent))/float(totalz)))
