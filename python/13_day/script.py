def read_data():
    file_reader = open('data.txt', 'r')

    my_timestamp = int(file_reader.readline()[:-1])

    bus_ids = file_reader.readline()[:-1].split(',')
    while 'x' in bus_ids:
        bus_ids.remove('x')
    bus_ids = sorted(bus_ids)

    bus_ids = list(map(int, bus_ids))

    dictionary = {'timestamp': my_timestamp, 'busses': bus_ids}

    return dictionary


def problem_one(data: dict):
    timestamp = data['timestamp']

    busses = data['busses']

    bus_id = 0
    difference = -1

    for bus in busses:
        initial = timestamp // bus
        departure = initial * bus
        while departure < timestamp:
            departure += bus
        new_difference = departure - timestamp
        if difference == -1:
            difference = new_difference
        if new_difference < difference:
            difference = new_difference
            bus_id = bus

    return bus_id * difference


def main():
    data = read_data()
    print(data)
    result_1 = problem_one(data)
    print(result_1)


if __name__ == "__main__":
    main()
