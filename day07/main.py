import csv
from dataclasses import dataclass


def parse():
    with open('input.txt') as f:
        reader = csv.reader(f)
        line = [line for line in reader][0]
        return [int(number) for number in line]


def update_list_param_v1(numbers, cursor):
    current_str = str(numbers[cursor])
    current = int(current_str[-1])

    immediate1 = len(current_str) > 2 and current_str[-3] == "1"
    immediate2 = len(current_str) > 3 and current_str[-4] == "1"
    parameter1 = numbers[cursor + 1]
    parameter2 = numbers[cursor + 2]
    parameter3 = numbers[cursor + 3]

    parameter1 = parameter1 if immediate1 else numbers[parameter1]
    parameter2 = parameter2 if immediate2 else numbers[parameter2]

    if current == 1:
        numbers[parameter3] = parameter1 + parameter2
    elif current == 2:
        numbers[parameter3] = parameter1 * parameter2


def update_list_param_v2(numbers, sys, input_number, cursor):
    current_str = str(numbers[cursor])
    current = int(current_str[-1])

    parameter1 = numbers[cursor + 1]
    immediate1 = len(current_str) > 2 and current_str[-3] == "1"

    if current == 3:
        numbers[parameter1] = sys if cursor == 0 else input_number  # terrible hack
    if current == 4:
        input_number = parameter1 if immediate1 else numbers[parameter1]
    return input_number


def update_list_param_v3(numbers, cursor):
    current_str = str(numbers[cursor])
    current = int(current_str[-1])

    immediate1 = len(current_str) > 2 and current_str[-3] == "1"
    immediate2 = len(current_str) > 3 and current_str[-4] == "1"
    parameter1 = numbers[cursor + 1]
    parameter2 = numbers[cursor + 2]
    parameter3 = numbers[cursor + 3]

    parameter1 = parameter1 if immediate1 else numbers[parameter1]
    parameter2 = parameter2 if immediate2 else numbers[parameter2]

    if current == 5:
        cursor = parameter2 if parameter1 != 0 else cursor + 3
    elif current == 6:
        cursor = parameter2 if parameter1 == 0 else cursor + 3
    elif current == 7:
        numbers[parameter3] = 1 if parameter1 < parameter2 else 0
        cursor += 4
    elif current == 8:
        numbers[parameter3] = 1 if parameter1 == parameter2 else 0
        cursor += 4
    return cursor


def update_list_part1(numbers: list, sys, input_number, cursor=0):
    if numbers[cursor] == 99:
        return input_number
    current_str = str(numbers[cursor])
    current = int(current_str[-1])

    if current in [1, 2]:
        update_list_param_v1(numbers, cursor)
        cursor += 4
    elif current in [3, 4]:
        input_number = update_list_param_v2(numbers, sys, input_number, cursor)
        cursor += 2
    elif current in [5, 6, 7, 8]:
        cursor = update_list_param_v3(numbers, cursor)

    return update_list_part1(numbers, sys, input_number, cursor)


def amplify_part1(numbers, a, b, c, d, e):
    new_numbers = numbers.copy()
    out_a = update_list_part1(new_numbers, a, 0)
    out_b = update_list_part1(new_numbers, b, out_a)
    out_c = update_list_part1(new_numbers, c, out_b)
    out_d = update_list_part1(new_numbers, d, out_c)
    out_e = update_list_part1(new_numbers, e, out_d)
    return out_e


def update_list_part2(numbers: list, sys, input_number, cursor=0):
    if numbers[cursor] == 99:
        return input_number, cursor
    current_str = str(numbers[cursor])
    current = int(current_str[-1])

    if current in [1, 2]:
        update_list_param_v1(numbers, cursor)
        cursor += 4
    elif current in [3, 4]:
        input_number = update_list_param_v2(numbers, sys, input_number, cursor)
        cursor += 2
        if current == 4:
            return input_number, cursor
    elif current in [5, 6, 7, 8]:
        cursor = update_list_param_v3(numbers, cursor)

    return update_list_part2(numbers, sys, input_number, cursor)


@dataclass
class Amp:
    cursor = 0
    out = 0
    numbers: list

    def __init__(self, numbers):
        self.numbers = numbers.copy()


def amplify_part2(numbers, a, b, c, d, e):
    amp_a, amp_b, amp_c, amp_d, amp_e = Amp(numbers), Amp(numbers), Amp(numbers), Amp(numbers), Amp(numbers),
    while amp_e.numbers[amp_e.cursor] != 99:
        amp_a.out, amp_a.cursor = update_list_part2(amp_a.numbers, a, amp_e.out, amp_a.cursor)
        amp_b.out, amp_b.cursor = update_list_part2(amp_b.numbers, b, amp_a.out, amp_b.cursor)
        amp_c.out, amp_c.cursor = update_list_part2(amp_c.numbers, c, amp_b.out, amp_c.cursor)
        amp_d.out, amp_d.cursor = update_list_part2(amp_d.numbers, d, amp_c.out, amp_d.cursor)
        amp_e.out, amp_e.cursor = update_list_part2(amp_e.numbers, e, amp_d.out, amp_e.cursor)
    return amp_e.out


def main():
    numbers = parse()
    results = []
    array_a = [0, 1, 2, 3, 4]
    for a in array_a:
        array_b = array_a.copy()
        array_b.remove(a)
        for b in array_b:
            array_c = array_b.copy()
            array_c.remove(b)
            for c in array_c:
                array_d = array_c.copy()
                array_d.remove(c)
                for d in array_d:
                    array_e = array_d.copy()
                    array_e.remove(d)
                    for e in array_e:
                        # thruster = amplify_part1(numbers, a, b, c, d, e)  #  part 1
                        thruster = amplify_part2(numbers, a + 5, b + 5, c + 5, d + 5, e + 5)  # part 2
                        # + 5 because now in [5, 6, 7, 8, 9]
                        results.append(thruster)

    print("max thruster value:", max(results))


if __name__ == "__main__":
    main()
