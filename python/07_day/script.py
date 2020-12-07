import csv


def read_data():
    data_dict = {}
    with open('data.csv') as data:
        csv_reader = csv.reader(data, delimiter='-')
        for row in csv_reader:
            without_dot = row[0][:-1]
            splitted_row = without_dot.split(' contain ')
            bag_type = splitted_row[0][:-1]
            contained_bags = splitted_row[1].split(', ')
            conained_bags_dict = {}
            for bag in contained_bags:
                split = bag.split(' ')
                amount = split[0]
                contained_bag_type = bag[len(amount) + 1:]
                if contained_bag_type[-1:] == 's':
                    contained_bag_type = contained_bag_type[:-1]
                if contained_bag_type != 'other bag':
                    conained_bags_dict[contained_bag_type] = amount
            if bag_type in data_dict:
                i = 1
                new_bag_type = bag_type + "_" + str(i)
                while new_bag_type in data_dict:
                    i += 1
                data_dict[new_bag_type] = conained_bags_dict
            else:
                data_dict[bag_type] = conained_bags_dict
        return data_dict


def problem_one(data: dict, starting_bag: str):
    final_list = []
    step_list = [starting_bag]
    new_list = []
    while step_list:
        for bag, rule in data.items():
            for contained_bag, amount in rule.items():
                if contained_bag in step_list:
                    new_list.append(bag)
        for bag in step_list:
            if bag not in final_list:
                final_list.append(bag)
        step_list = []
        for bag in new_list:
            if bag not in final_list:
                step_list.append(bag)
        new_list = []

    print(final_list)
    print(len(final_list) - 1)


def problem_two(bag_type: str, bags_used: int):
    current_bag_dict = all_data[bag_type]
    if len(current_bag_dict.items()) == 0:
        return [[], bags_used]
    else:
        bag_sum = bags_used
        individiual_bags = []
        for bag, amount in current_bag_dict.items():
            part_result = problem_two(bag, int(amount))
            bag_sum += bags_used * part_result[1]
            individiual_bags += part_result[0]
            if bag not in individiual_bags:
                individiual_bags.append(bag)
        return [individiual_bags, bag_sum]


def print_dict(data: dict):
    for key, elem in data.items():
        print(key + ": ", end=" ")
        print(elem)


if __name__ == "__main__":
    all_data = read_data()
    print_dict(all_data)

    problem_one(all_data, "shiny gold bag")
    result = problem_two('shiny gold bag', 1)
    print(result[0])
    # remove shiny gold bag
    print(result[1] - 1)
