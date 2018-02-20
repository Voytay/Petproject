""" f. odczytuje z pliku
parametry:
filename -> "expenses.txt" 
zwraca:
data = [[l.p,kwota,kategoria,opis,data]]"""

def data_import(filename):
    with open(filename, "r") as file:
        content = file.readlines()
    content = list(map(str.strip, content))
    content = [element.split(",") for element in content]
    return content


""" funkcja nadpisuje dane (mode = w) w pliku o podanej przez użytkownika nazwie 
    parametry:
    data -> lista list, 
    filename -> earnings.txt / expences.txt / categories.txt """

def data_export(data, filename):
    with open(filename, "w") as file:
        for i in range(len(data)):
            data[i] = list(map(str, data[i]))
            row = ",".join(data[i])
            file.write(row + "\n")

