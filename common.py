def sort():

    myfile = [["xxx,xxx,shopp,xxx,2015.02.30"],["xxx,xxx,sx,xxx,2016.10.04"]]
    list_to_check = split_elements(myfile)
    category = 2
    date = 4

    sort_option = input("Do you want sort by date or category [d/c]?: ")

    if sort_option == "d":

        sort_by_date(list_to_check, date)

    elif sort_option == "c":
        get_category = input("Enter category: ") 
        sort_by_date = input("Do you want to display at specifc time [y/n]: ?")
        for elements in list_to_check:             
            if elements[category] == get_category:
                if sort_by_date == "n":
                    print(elements)

                elif sort_by_date == "y":
                    sort_by_date(list_to_check, date)

def sort_by_date(list_to_check, date):
    date_from = input("Give the year to check from [yyyy.mm.dd]: ")
    date_to = input("Give the year to check to[yyyy.mm.dd]: ")

    for elements in list_to_check:
        if elements[date][:4] >= date_from[:4] and elements[date][:4] <= date_to[:4]:
            if elements[date][5:7] >= date_from[5:7] and elements[date][5:7] <= date_to[5:7]:
                if elements[date][8:10] >= date_from[8:10] and elements[date][8:10] <= date_to[8:10]:
                    print(elements)

def split_elements(myfile):
    list_to_check = []
    for elements in myfile:
        for i in elements:
            i = i.split(",")
            list_to_check.append(i)
    return list_to_check

sort()
