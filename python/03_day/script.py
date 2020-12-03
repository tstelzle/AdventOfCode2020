import csv

list_data = []

def read_data():
    with open('data.csv') as data:
        csv_reader = csv.reader(data,delimiter=' ')
        for row in csv_reader:
            horizontal = split(row[0])
            list_data.append(horizontal)

def print_matrix(list):
    for horizontal in list:
        for item in horizontal:
            print(item, end="")
        print()

def split(word):
    return [char for char in word]

def end_to_end(right: int, down: int):
    horizontal = 0
    vertical = 0
    vertical_max = len(list_data) -1
    horizontal_max = len(list_data[0]) -1
    trees = 0

    #Read first symbol
    trees += is_symbol_tree(list_data[vertical][horizontal])

    while vertical < vertical_max:
        if horizontal_max - horizontal >= right:
            horizontal += right
        else:
            horizontal = (-1 * (horizontal_max - horizontal - right)) -1
        vertical += down
        trees += is_symbol_tree(list_data[vertical][horizontal])

    return trees

def is_symbol_tree(symbol):
    if symbol == '#':
        return 1
    else:
        return 0

def main():
    read_data()
    #print_matrix(list_data)
    solution_1 = end_to_end(1,1)
    solution_2 = end_to_end(3,1)
    solution_3 = end_to_end(5,1)
    solution_4 = end_to_end(7,1)
    solution_5 = end_to_end(1,2)
    print(solution_1)
    print(solution_2)
    print(solution_3)
    print(solution_4)
    print(solution_5)

    print(solution_1 * solution_2 * solution_3 * solution_4 * solution_5)

if __name__ == "__main__":
    main()