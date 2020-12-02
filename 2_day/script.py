import csv

list_data = []

def read_data():
    with open('data.csv') as data:
        csv_reader = csv.reader(data, delimiter=' ')
        line_count = 0
        for row in csv_reader:
            min_max = row[0].split('-')
            min = min_max[0]
            max = min_max[1]
            letter = row[1].split(':')
            list_data.append({'min': int(min), 'max': int(max), 'letter': letter[0], 'password': row[2]})
            line_count += 1

def print_list_of_dicts(dict_list):
    for elem in dict_list:
        print(elem)

def count_valid_pw_1():
    counter_valid = 0
    counter_non_valid = 0
    for elem in list_data:
        count_char = elem['password'].count(elem['letter'])
        if elem['min'] <= count_char and elem['max'] >= count_char:
            counter_valid += 1
        else:
            counter_non_valid += 1
    print('Non valid 1: ' + str(counter_non_valid))
    return counter_valid

def count_valid_pw_2():
    counter_valid = 0
    valid_list = []
    counter_non_valid = 0
    non_valid_list = []
    for elem in list_data:
        if (elem['password'][elem['min']-1] == elem['letter'] and elem['password'][elem['max']-1] != elem['letter']) or (elem['password'][elem['min']-1] != elem['letter'] and elem['password'][elem['max']-1] == elem['letter']):
            valid_list.append(elem)
            counter_valid += 1
        else:
            non_valid_list.append(elem)
            counter_non_valid += 1
    '''
    print(' - valid list -')
    print_list_of_dicts(valid_list)
    print(' - non valid list - ')
    print_list_of_dicts(non_valid_list)
    '''
    print('Non valid 2: ' + str(counter_non_valid))
    return counter_valid

def main():
    read_data()
    print('Passwords: ' + str(len(list_data)))
    print('Valid 1: ' + str(count_valid_pw_1()))
    print('Valid 2: ' + str(count_valid_pw_2()))

if __name__ == "__main__":
    main()

