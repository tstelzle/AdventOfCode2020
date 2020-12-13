def read_data():
    data = []
    file_reader = open("data.txt", "r")
    for line in file_reader:
        data.append(int(line))

    return data


def sum_xmas(data: list, sum_value: int):
    for value_1 in data:
        for value_2 in data:
            if value_1 != value_2 and value_1 + value_2 == sum_value:
                return True

    return False


def problem_one(data: list):
    current_pointer = 25
    xmas = True

    while xmas:
        start_pointer = current_pointer - 25
        xmas = sum_xmas(data[start_pointer: current_pointer], data[current_pointer])
        current_pointer += 1

    return data[current_pointer - 1]


def check_list_length(data: list, problem_solution: int, list_length: int):
    sum_found = False
    current_pointer = 0
    solution_list = []

    while not sum_found:
        print(str(current_pointer) + " : " + str(list_length))
        if current_pointer + list_length > len(data):
            sum_found = True
        else:
            part_list = data[current_pointer: (current_pointer + list_length)]
            sum_part_list = sum(part_list)
            if problem_solution == sum_part_list:
                solution_list = data[current_pointer:current_pointer + list_length]
                sum_found = True
            current_pointer += 1

    if len(solution_list) != 0:
        max_solution_list = max(solution_list)
        min_solution_list = min(solution_list)
        return max_solution_list + min_solution_list
    else:
        return 0


def problem_two(data: list, problem_solution: int):
    for list_length in range(2, len(data)):
        result = check_list_length(data, problem_solution, list_length)
        if result != 0:
            return result


def main():
    data = read_data()

    result_1 = problem_one(data)
    result_2 = problem_two(data, result_1)

    print(result_1)
    print(result_2)


if __name__ == "__main__":
    main()
