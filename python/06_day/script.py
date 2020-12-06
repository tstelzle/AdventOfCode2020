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
    sum = 0
    list_sum = []
    for group in data:
        single_answers = []
        for key, person_answer in group.items():
            for answer in person_answer:
                if answer not in single_answers:
                    single_answers.append(answer)
        list_sum.append(single_answers)
        sum += len(single_answers)

    print(list_sum)
    return sum

def problem_two(data: list):
    sum = 0
    list_sum = []
    for group in data:
        group_answers = []
        for key,person_answer in group.items():
            for answer in person_answer:
                taking_answer = True
                for key, person_answer in group.items():
                    if answer not in person_answer:
                        taking_answer = False
                if taking_answer and answer not in group_answers:
                    group_answers.append(answer)
        list_sum.append(group_answers)
        sum += len(group_answers)

    print(list_sum)
    return sum

def main():
    data = read_data()
    solution_1 = problem_one(data)
    print(solution_1)

    solution_2 = problem_two(data)
    print(solution_2)

if __name__ == "__main__":
    main()
