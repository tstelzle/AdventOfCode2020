def read_data():
    file_reader = open('data.txt', 'r')

    my_timestamp = int(file_reader.readline()[:-1])

    bus_ids = file_reader.readline().split(',')

    dictionary = {'timestamp': my_timestamp, 'busses': bus_ids}

    return dictionary


def problem_one(data: dict):
    timestamp = data['timestamp']

    busses = data['busses']

    bus_id = 0
    difference = -1

    for bus in busses:
        if bus != 'x':
            bus = int(bus)
            initial = timestamp // bus
            departure = (initial + 1) * bus
            new_difference = departure - timestamp
            if difference == -1:
                difference = new_difference
            if new_difference < difference:
                difference = new_difference
                bus_id = bus

    return bus_id * difference


def pos_checker(timestamp: int, busses: list, pos):
    if (timestamp + pos) % int(busses[pos]) == 0:
        return True
    else:
        return False


def problem_two(data: dict):
    busses = data['busses']
    timestamp = 0
    timestamp_found = False
    adding = 1
    switch_adding = True

    bus_pos = [busses.index(x) for x in busses if x != 'x']
    max_pos = 0
    for x in range(0, len(bus_pos)):
        if int(busses[bus_pos[x]]) > int(busses[bus_pos[max_pos]]):
            max_pos = x

    while not timestamp_found:
        timestamp += adding
        print(timestamp)
        short_pos_checker = lambda lst: pos_checker(timestamp, busses, lst)
        departures = list(map(short_pos_checker, bus_pos))
        if all(departures):
            timestamp_found = True
        if switch_adding:
            if departures[max_pos]:
                adding = int(busses[bus_pos[max_pos]])
                switch_adding = False
            else:
                if timestamp % int(busses[bus_pos[0]]) == 0:
                    adding = int(busses[bus_pos[0]])

    return timestamp


def main():
    data = read_data()
    print(data)

    result_1 = problem_one(data)
    print(result_1)

    result_2 = problem_two(data)
    print(result_2)


if __name__ == "__main__":
    main()
