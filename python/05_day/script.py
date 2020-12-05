import csv


def read_data():
    list_data = []
    with open('data.csv') as data:
        csv_reader = csv.reader(data, delimiter=' ')
        for row in csv_reader:
            list_data.append(row[0])

    return list_data


def calculate_seat(sequence: str):
    row_min = 0
    row_max = 127
    row = sequence[:-3]

    column_min = 0
    column_max = 7
    column = sequence[7:]

    for i in range(0, len(row)):
        val = (row_max + row_min) // 2
        if row[i] == 'F':
            row_max = val
        elif row[i] == 'B':
            row_min = val + 1

    for i in range(0, len(column)):
        val = (column_max + column_min) // 2
        if column[i] == 'L':
            column_max = val
        elif column[i] == 'R':
            column_min = val + 1

    if column_min == column_max and row_min == row_max:
        return [row_max, column_max]
    else:
        print('There is something wrong.')
        print(row_min, row_max, column_min, column_max)
        return []


def calculate_seat_id(data: list):
    return data[0] * 8 + data[1]


def problem_one(data: list):
    seat_id_max = 0
    seat_ids = []
    for elem in data:
        seat_numbers = calculate_seat(elem)
        new_seat_id_max = calculate_seat_id(seat_numbers)
        seat_ids.append(new_seat_id_max)
        if new_seat_id_max > seat_id_max:
            seat_id_max = new_seat_id_max

    return seat_ids


def problem_two(data: list):
    for row in range(0, 127):
        for column in range(0, 7):
            seat_id = row * 8 + column
            if seat_id not in data:
                if seat_id + 1 in data and seat_id - 1 in data:
                    return seat_id


def main():
    data = read_data()
    solution_1 = problem_one(data)
    print(max(solution_1))
    print(problem_two(solution_1))


if __name__ == "__main__":
    main()
