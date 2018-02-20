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