import csv

list_data = []


def read_data():
    with open('data.csv') as data:
        csv_reader = csv.reader(data, delimiter=' ')
        dict_items = {}
        for row in csv_reader:
            if not row:
                list_data.append(dict_items)
                dict_items = {}
            else:
                for elem in row:
                    splitted_elem = elem.split(':')
                    key = splitted_elem[0]
                    data = splitted_elem[1]
                    dict_items[key] = data
        list_data.append(dict_items)


def problem_one():
    necessary_items = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
    valid_passports = []
    for passport in list_data:
        passport_valid = True
        dict_keys = list(passport.keys())
        for item in necessary_items:
            if item not in dict_keys:
                passport_valid = False
                break
        if passport_valid:
            valid_passports.append(passport)

    return valid_passports


def problem_two(valid_passports_1: list):
    valid_passports_2 = []
    for passport in valid_passports_1:
        byr = True
        iyr = True
        eyr = True
        hgt = True
        hcl = True
        ecl = True
        pid = True
        cid = True
        for key, data in passport.items():
            if key == 'byr':
                byr = check_number(data, 4, 1920, 2020)
            elif key == 'iyr':
                iyr = check_number(data, 4, 2010, 2020)
            elif key == 'eyr':
                eyr = check_number(data, 4, 2020, 2030)
            elif key == 'hgt':
                hgt = check_hgt(data)
            elif key == 'hcl':
                hcl = check_hcl(data)
            elif key == 'ecl':
                ecl = check_ecl(data)
            elif key == 'pid':
                pid = check_pid(data)
            elif key == 'cid':
                cid = True
            else:
                print('Key not given.')
        if byr and iyr and eyr and hgt and hcl and ecl and pid and cid:
            valid_passports_2.append(passport)

    return valid_passports_2


def check_pid(item: str):
    if len(item) != 9:
        return False
    return True


def check_ecl(item: str):
    valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if item not in valid_colors:
        return False
    return True


def check_number(item: str, length: int, min_value: int, max_value: int):
    if len(item) != length:
        return False
    birth_year = int(item)
    if birth_year < min_value or birth_year > max_value:
        return False
    return True


def check_hgt(item: str):
    if len(item) > 2:
        height = int(item[:-2])
    else:
        return False
    if item[-2:] == 'cm':
        if 150 <= height <= 193:
            return True
    elif item[-2:] == 'in':
        if 59 <= height <= 76:
            return True
    return False


def check_hcl(item: str):
    if item[:1] != '#':
        return False
    if len(item) != 7:
        return False
    return True


def print_data(data_list: list):
    for passport in data_list:
        print(passport)


def print_data_keys():
    for passport in list_data:
        print(list(passport.keys()))


def print_keys_of_dict(dicitonary: dict):
    print(list(dicitonary.keys()))


if __name__ == "__main__":
    read_data()
    solution_1 = problem_one()
    print_data(solution_1)
    print(len(solution_1))
    solution_2 = problem_two(solution_1)
    print_data(solution_2)
    print(len(solution_2))
