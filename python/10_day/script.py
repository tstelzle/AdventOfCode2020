def read_data():
    file_reader = open("data.txt", "r")
    data = []
    for line in file_reader:
        data.append(int(line))

    max_data = max(data)
    # Phone Adapter
    data.append(max_data + 3)
    # Charger Adapter
    data.append(0)

    return data


def problem_one(data: list):
    data_2 = sorted(data)
    differences = {}
    print(data_2)
    for i in range(1, len(data_2)):
        difference = data_2[i] - data_2[i - 1]
        if difference not in differences.keys():
            differences[difference] = 1
        else:
            differences[difference] += 1

    print(differences)
    return differences[1] * differences[3]


def main():
    data = read_data()
    print(data)
    print(len(data))

    result_1 = problem_one(data)
    print(result_1)


if __name__ == "__main__":
    main()
