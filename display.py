def print_menu(data):
    i = 1
    for element in data:
        print(i, "----->", element.title())
        i += 1


def print_message(message):
    print(message)


def print_list(data, header):
    print(header)
    for element in data:
        print(element)
    print()


def print_table(data):
    title = ['Id', 'Amount', 'Categories', 'Details', 'Year', 'Month', 'Day']
    max_lenght = []

    for i in range(len(title)):
        max_len_in_column = len(title[i])

        for j in range(len(data)):
            if len(str(data[j][i])) > max_len_in_column:
                max_len_in_column = len(str(data[j][i]))

        max_lenght.append(max_len_in_column)

    extra_sign = 2*len(title)+2
    width = sum(max_lenght) + extra_sign

    row = []
    for i in range(len(title)):
        row.append("| " + title[i].center(max_lenght[i]))
    row.append(" |")
    print("".join(row))
    print("="*width)

    for item in data:
        row = []
        for i in range(len(title)):
            row.append("| " + str(item[i]).rjust(max_lenght[i]))
        row.append(" |")
        print("".join(row))


def total(filename):
    total = 0
    data = data_manager.data_import(filename)
    for element in data:
        total += float(element[1])
    return str(total)


def print_percentage_spent():
    spent = total('expenses.txt')
    totalz = total('earnings.txt')
    print_message("Total spent: " + spent + ' of ' + totalz + \
    " | Left: {:.2%}".format((float(totalz)-float(spent))/float(totalz)))
