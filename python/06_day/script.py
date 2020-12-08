import csv


def read_data():
    list_data = []
    with open('data.csv') as data:
        csv_reader = csv.reader(data)
        group = {}
        person = 0
        for row in csv_reader:
            if not row:
                list_data.append(group)
                group = {}
                person = 0
            else:
                group[person] = row[0]
                person += 1
        list_data.append(group)

    return list_data


def print_groups(data: list):
    for elem in data:
        print(elem)


def problem_one(data: list):
    answer_sum = 0
    list_sum = []
    for group in data:
        single_answers = []
        for key, person_answer in group.items():
            for answer in person_answer:
                if answer not in single_answers:
                    single_answers.append(answer)
        list_sum.append(single_answers)
        answer_sum += len(single_answers)

    print(list_sum)
    return answer_sum


def problem_two(data: list):
    answer_sum = 0
    list_sum = []
    for group in data:
        group_answers = []
        for key, person_answer in group.items():
            for answer in person_answer:
                taking_answer = True
                for key_2, person_answer_2 in group.items():
                    if answer not in person_answer_2:
                        taking_answer = False
                if taking_answer and answer not in group_answers:
                    group_answers.append(answer)
        list_sum.append(group_answers)
        answer_sum += len(group_answers)

    print(list_sum)
    return answer_sum


def read_data_2():
    data_list = []
    with open('data.csv') as data:
        csv_reader = csv.reader(data, delimiter=' ')
        person_count = 0
        answer_string = ""
        for row in csv_reader:
            if not row:
                group_data = str(person_count) + "," + answer_string
                data_list.append(group_data)
                person_count = 0
                answer_string = ""
            else:
                person_count += 1
                answer_string += row[0]
        group_data = str(person_count) + "," + answer_string
        data_list.append(group_data)

    return data_list


def problem_two_2(data: list):
    answer_sum = 0
    for group in data:
        splitted = group.split(',')
        person_count = int(splitted[0])
        answer_string = splitted[1]
        all_answered = [answer for answer in answer_string if answer_string.count(answer) == person_count]
        all_answered_set = set(all_answered)
        answer_sum += len(all_answered_set)

    return answer_sum


def main():
    data = read_data()
    solution_1 = problem_one(data)
    print(solution_1)

    solution_2 = problem_two(data)
    print(solution_2)

    data_2 = read_data_2()
    print(data_2)
    solution_2_2 = problem_two_2(data_2)
    print(solution_2_2)


if __name__ == "__main__":
    main()
