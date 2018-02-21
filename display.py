def print_menu(data):
    i = 1
    for element in data:
        print(i, "----->", element.title())
        i += 1


def print_data(data, header):
    print(header)
    for element in data:
        print(" | ".join(element))


def print_message(message):
    print(message)


def print_table(data, title):
    
    max_lenght = []
    for i in range(len(title)):
        for j in range(len(data)):
            max_len_in_column = len(title[i])

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

title = ["id", "kwota", "kategoria"]
data = [["1","25.00","shopping"], 
        ["2","5.00","transport"],
        ["3","56.50","shopping"]]
tabelka = print_table(data, title)

