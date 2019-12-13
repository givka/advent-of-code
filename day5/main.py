import csv


def parse():
    with open('input.txt') as f:
        reader = csv.reader(f)
        line = [line for line in reader][0]
        return [int(number) for number in line]


def update_list_old(numbers, cursor):
    current_str = str(numbers[cursor])
    current = int(current_str[-1])

    immediate1 = len(current_str) > 2 and current_str[-3] == "1"
    immediate2 = len(current_str) > 3 and current_str[-4] == "1"
    parameter1 = numbers[cursor + 1]
    parameter2 = numbers[cursor + 2]
    parameter3 = numbers[cursor + 3]

    if current == 1:
        numbers[parameter3] = (parameter1 if immediate1 else numbers[parameter1]) \
                              + (parameter2 if immediate2 else numbers[parameter2])
    elif current == 2:
        numbers[parameter3] = (parameter1 if immediate1 else numbers[parameter1]) \
                              * (parameter2 if immediate2 else numbers[parameter2])


def update_list_new(numbers, input_number, cursor):
    current_str = str(numbers[cursor])
    current = int(current_str[-1])

    parameter1 = numbers[cursor + 1]
    immediate1 = len(current_str) > 2 and current_str[-3] == "1"

    if current == 3:
        numbers[parameter1] = input_number
        input_number = 0
    elif current == 4:
        input_number = parameter1 if immediate1 else numbers[parameter1]
    return input_number


def update_list(numbers: list, input_value: int, cursor=0):
    if numbers[cursor] == 99:
        return input_value
    current_str = str(numbers[cursor])
    current = int(current_str[-1])

    if current == 1 or current == 2:
        update_list_old(numbers, cursor)
        cursor += 4
    elif current == 3 or current == 4:
        input_value = update_list_new(numbers, input_value, cursor)
        cursor += 2

    return update_list(numbers, input_value, cursor)


def main():
    numbers = parse()
    print("output:", update_list(numbers, 1))


if __name__ == "__main__":
    main()
