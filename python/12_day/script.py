import copy


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

    print('North Value: ' + str(north_value))
    print('East Value: ' + str(east_value))
    print('Sum: ' + str(north_value + east_value))

    return ship_position


def reformat_coordinate(coordinate_dict: dict):
    north = 0
    east = 0
    south = 0
    west = 0
    if (coordinate_dict["N"] - coordinate_dict["S"]) > 0:
        north = coordinate_dict["N"] - coordinate_dict["S"]
    if (coordinate_dict["S"] - coordinate_dict["N"]) > 0:
        south = coordinate_dict["S"] - coordinate_dict["N"]
    if (coordinate_dict["E"] - coordinate_dict["W"]) > 0:
        east = coordinate_dict["E"] - coordinate_dict["W"]
    if (coordinate_dict["W"] - coordinate_dict["E"]) > 0:
        west = coordinate_dict["W"] - coordinate_dict["E"]

    coordinate_dict["N"] = north
    coordinate_dict["E"] = east
    coordinate_dict["S"] = south
    coordinate_dict["W"] = west

    return coordinate_dict


def cardinal_to_int(cardinal: str):
    if cardinal == "N":
        return 1
    elif cardinal == "E":
        return 2
    elif cardinal == "S":
        return 3
    elif cardinal == "W":
        return 4


def int_to_cardinal(cardinal_int: int):
    if cardinal_int == 1:
        return "N"
    elif cardinal_int == 2:
        return "E"
    elif cardinal_int == 3:
        return "S"
    elif cardinal_int == 4:
        return "W"


def cardinal_rotate(cardinal: str, left: bool):
    if left:
        new_cardinal_int = cardinal_to_int(cardinal) - 1
        if new_cardinal_int == 0:
            new_cardinal_int = 4
        return int_to_cardinal(new_cardinal_int)
    else:
        new_cardinal_int = cardinal_to_int(cardinal) + 1
        if new_cardinal_int == 5:
            new_cardinal_int = 1
        return int_to_cardinal(new_cardinal_int)


def problem_two(instructions: dict):
    waypoint = {"N": 1, "E": 10, "S": 0, "W": 0}
    ship_pos = {"N": 0, "E": 0, "S": 0, "W": 0}

    for key, value in instructions.items():

        waypoint = reformat_coordinate(waypoint)
        ship_pos = reformat_coordinate(ship_pos)

        if value["direction"] == "F":
            for cardinal, position in waypoint.items():
                ship_pos[cardinal] += value["amount"] * position
        elif value["direction"] == "N":
            waypoint["N"] += value["amount"]
        elif value["direction"] == "E":
            waypoint["E"] += value["amount"]
        elif value["direction"] == "S":
            waypoint["S"] += value["amount"]
        elif value["direction"] == "W":
            waypoint["W"] += value["amount"]
        elif value["direction"] == "R" or value["direction"] == "L":
            iterations = value["amount"] // 90
            while iterations != 0:
                left = True if value["direction"] == "L" else False
                waypoint_copy = copy.deepcopy(waypoint)
                for cardinal, position in waypoint_copy.items():
                    waypoint[cardinal_rotate(cardinal, left)] = waypoint_copy[cardinal]
                iterations -= 1

    ship_pos = reformat_coordinate(ship_pos)

    north_value = ship_pos["S"] if ship_pos["N"] == 0 else ship_pos["N"]
    print('North Value: ' + str(north_value))
    east_value = ship_pos["E"] if ship_pos["W"] == 0 else ship_pos["W"]
    print('East Value: ' + str(east_value))
    print('Sum: ' + str(north_value + east_value))

    return ship_pos


def main():
    instructions = read_data()

    result_1 = problem_one(instructions)
    print(result_1)

    result_2 = problem_two(instructions)
    print(result_2)


if __name__ == "__main__":
    main()
