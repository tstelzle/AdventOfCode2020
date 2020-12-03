import csv
import sys

list_data = []

def read_data():
    with open('data.csv') as data:
        csv_reader = csv.reader(data, delimiter=',')
        for row in csv_reader:
            list_data.append(int(row[0]))

def two_elems():
    for elem in list_data:
        for elem_2 in list_data:
            if elem + elem_2 == 2020:
                return [elem, elem_2]
    return []

def three_elems():
    for elem in list_data:
        for elem_2 in list_data:
            for elem_3 in list_data:
                if elem + elem_2 + elem_3 == 2020:
                    return [elem, elem_2, elem_3]
    return []

def print_result(my_list):
    product = 1
    for i in range(len(my_list)):
        product *= my_list[i]
        print(str(i+1) + ": " + str(my_list[i]))
    print('Product: ' + str(product))

def main():
    print('test')
    elems = 2
    if len(sys.argv) > 1:
        elems = int(sys.argv[1])

    read_data()

    if(elems == 2):
        my_list = two_elems()
    elif(elems == 3):
        my_list = three_elems()
    else:
        print('This parameter is not supported.')
        return

    print_result(my_list)

if __name__ == "__main__":
    main()