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