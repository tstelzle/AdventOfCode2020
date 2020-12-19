import copy

EMPTY = 0
OCCUPIED = 1
FLOOR = 0


def read_data():
    file_reader = open("data.txt", "r")
    rows = []
    for line in file_reader:
        row = []
        for seat in line:
            if seat != '\n':
                row.append(seat)
        rows.append(row)

    return rows


def print_seating_area(area: list):
    for row in area:
        for column in row:
            print(column, end='')
        print()


def get_current_state(area: list, row: int, column: int, get_value: bool, problem_two: bool = False,
                      direction: str = ''):
    seat_char = area[row][column]
    if problem_two:
        if direction:
            not_end_of_list = True
            while seat_char == '.' and not_end_of_list:
                if direction == 'left':
                    if column > 0:
                        column -= 1
                    else:
                        not_end_of_list = False
                elif direction == 'right':
                    if column + 1 < len(area[row]):
                        column += 1
                    else:
                        not_end_of_list = False
                elif direction == 'bottom':
                    if row + 1 < len(area):
                        row += 1
                    else:
                        not_end_of_list = False
                elif direction == 'bottom_left':
                    if column > 0 and row + 1 < len(area):
                        column -= 1
                        row += 1
                    else:
                        not_end_of_list = False
                elif direction == 'bottom_right':
                    if row + 1 < len(area):
                        row += 1
                        if column + 1 < len(area[row]):
                            column += 1
                        else:
                            not_end_of_list = False
                            row -= 1
                    else:
                        not_end_of_list = False
                elif direction == 'top':
                    if row > 0:
                        row -= 1
                    else:
                        not_end_of_list = False
                elif direction == 'top_left':
                    if column > 0 and row > 0:
                        row -= 1
                        column -= 1
                    else:
                        not_end_of_list = False
                elif direction == 'top_right':
                    if row > 0:
                        row -= 1
                        if column + 1 < len(area[row]):
                            column += 1
                        else:
                            not_end_of_list = False
                            row += 1
                    else:
                        not_end_of_list = False
                seat_char = area[row][column]

    if get_value:
        if seat_char == 'L':
            return EMPTY
        elif seat_char == '#':
            return OCCUPIED
        elif seat_char == '.':
            return FLOOR
    else:
        return seat_char


def get_new_state(area: list, row: int, column: int, problem_two: bool = False):
    if problem_two:
        seat_value_compare = 5
    else:
        seat_value_compare = 4

    current_seat = get_current_state(area, row, column, False, problem_two, '')
    if current_seat == '.':
        return '.'

    top = EMPTY
    bottom = EMPTY
    left = EMPTY
    right = EMPTY
    top_left = EMPTY
    top_right = EMPTY
    bottom_left = EMPTY
    bottom_right = EMPTY

    if row > 0:
        top = get_current_state(area, row - 1, column, True, problem_two, 'top')
        if column > 0:
            top_left = get_current_state(area, row - 1, column - 1, True, problem_two, 'top_left')
        if column + 1 < len(area[row]):
            top_right = get_current_state(area, row - 1, column + 1, True, problem_two, 'top_right')

    if column > 0:
        left = get_current_state(area, row, column - 1, True, problem_two, 'left')
    if column + 1 < len(area[row]):
        right = get_current_state(area, row, column + 1, True, problem_two, 'right')

    if row + 1 < len(area):
        bottom = get_current_state(area, row + 1, column, True, problem_two, 'bottom')
        if column > 0:
            bottom_left = get_current_state(area, row + 1, column - 1, True, problem_two, 'bottom_left')
        if column + 1 < len(area[row]):
            bottom_right = get_current_state(area, row + 1, column + 1, True, problem_two, 'bottom_right')

    seat_value = top + left + bottom + right + top_left + top_right + bottom_left + bottom_right

    if current_seat == 'L' and seat_value == 0:
        return '#'
    elif current_seat == '#' and seat_value >= seat_value_compare:
        return 'L'
    else:
        return current_seat


def count_symbols(area: list):
    symbols = {}
    for row in area:
        for column in row:
            if column not in symbols.keys():
                symbols[column] = 1
            else:
                symbols[column] += 1

    return symbols


def problem(area: list, problem_two: bool = False):
    current_seating_area = copy.deepcopy(area)
    empty_list = []

    for row_counter in current_seating_area:
        empty_list.append(['.' for i in range(0, len(row_counter))])

    new_seating_area = copy.deepcopy(empty_list)

    while current_seating_area != new_seating_area:
        if new_seating_area != empty_list:
            current_seating_area = copy.deepcopy(new_seating_area)

        for row in range(0, len(current_seating_area)):
            for column in range(0, len(current_seating_area[row])):
                new_seating_area[row][column] = get_new_state(current_seating_area, row, column, problem_two)

    return new_seating_area


def main():
    area = read_data()

    result_1 = problem(area)
    # print_seating_area(result_1)
    print(count_symbols(result_1))

    result_2 = problem(area, True)
    # print_seating_area(result_2)
    print(count_symbols(result_2))


if __name__ == "__main__":
    main()
