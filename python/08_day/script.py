import concurrent.futures
import copy


def read_data():
    file_reader = open("data.txt", "r")

    data_dict = {}
    line_count = 0
    for line in file_reader:
        split_line = line.split(" ")
        data_dict[line_count] = {"operation": split_line[0], "value": int(split_line[1]), "amount": 0}
        line_count += 1

    return data_dict


def problem_one(data_dict: dict):
    pointer = 0
    accumulator = 0
    programming_running = True
    while programming_running:
        value = data_dict[pointer]
        if value["amount"] == 1:
            return [pointer, accumulator]
        else:
            data_dict[pointer]["amount"] += 1
            if data_dict[pointer]["operation"] == "acc":
                accumulator += data_dict[pointer]["value"]
                pointer += 1
            elif data_dict[pointer]["operation"] == "jmp":
                pointer += data_dict[pointer]["value"]
            else:
                pointer += 1
            if pointer == len(data_dict.keys()):
                return [pointer - 1, accumulator]

    return [pointer, accumulator]


def problem_two(data_dict: dict):
    pointer_to_reach = len(data_dict.keys()) - 1
    for key, elem in data_dict.items():
        if elem["operation"] == "jmp" or elem["operation"] == "nop":
            copy_dict = copy.deepcopy(data_dict)
            if elem["operation"] == "jmp":
                copy_dict[key]["operation"] = "nop"
            else:
                copy_dict[key]["operation"] = "jmp"
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(problem_one, copy_dict)
                future_output = future.result()
                if future_output[0] == pointer_to_reach:
                    return future_output


def print_dict(data_dict: dict):
    for key, elem in data_dict.items():
        print(key, end="")
        print(":", end="")
        print(elem)


def main():
    data_dict = read_data()
    print_dict(data_dict)

    print(problem_one(data_dict))

    data_dict = read_data()
    print(problem_two(data_dict))


if __name__ == "__main__":
    main()
