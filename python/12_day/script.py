def integer_to_direction(direction_int: int):
    if direction_int == 0:
        return 'N'
    elif direction_int == 90:
        return 'E'
    elif direction_int == 180:
        return 'S'
    elif direction_int == 270:
        return 'W'


def direction_to_integer(direction: str):
    if direction == "N":
        return 0
    elif direction == 'E':
        return 90
    elif direction == 'S':
        return 180
    else:
        return 270


def read_data():
    file_reader = open("data.txt", 'r')
    instructions = {}
    instruction_counter = 0
    for line in file_reader:
        instructions[instruction_counter] = {"direction": line[:1], "amount": int(line[1:-1])}
        instruction_counter += 1

    return instructions


def print_dict(input_dict: dict):
    for key, value in input_dict.items():
        print(key, end="")
        print(": ", end="")
        print(value)


def problem_one(instructions: dict):
    ship_position = {"facing": 90, "N": 0, "E": 0, "W": 0, "S": 0}

    for key, value in instructions.items():
        if value["direction"] == "F":
            ship_position[integer_to_direction(ship_position["facing"])] += value["amount"]
        elif value["direction"] == "R":
            ship_position["facing"] += value["amount"]
            ship_position["facing"] = ship_position["facing"] % 360
        elif value["direction"] == "L":
            ship_position["facing"] -= value["amount"]
            if ship_position["facing"] < 0:
                ship_position["facing"] = 360 + ship_position["facing"]
        elif value["direction"] == 'N':
            ship_position['N'] += value["amount"]
        elif value["direction"] == 'E':
            ship_position['E'] += value["amount"]
        elif value["direction"] == 'S':
            ship_position['S'] += value["amount"]
        elif value["direction"] == 'W':
            ship_position['W'] += value["amount"]

    north_value = ship_position['N'] - ship_position['S']
    if north_value < 0:
        north_value *= -1
    east_value = ship_position['E'] - ship_position['W']
    if east_value < 0:
        east_value *= -1

    print('Nort Value: ' + str(north_value))
    print('East Value: ' + str(east_value))
    print('Sum: ' + str(north_value + east_value))

    return ship_position


def main():
    instructions = read_data()

    result_1 = problem_one(instructions)
    print(result_1)


if __name__ == "__main__":
    main()
