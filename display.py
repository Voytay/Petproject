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
            if len(data[j][i]) > max_len_in_column:
                max_len_in_column = len(data[j][i])
            
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
            row.append("| " + item[i].rjust(max_lenght[i]))
        row.append(" |")
        print("".join(row))

data = [['2d3S', '25.00', 'Categories', 'dggyht bhujnhg hhuyuu', 'Year', 'Month', 'Day'], 
['9a3E', '5.0', 'Categories', 'gils', 'Year', 'Month', 'Day']]

print_table(data)

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
