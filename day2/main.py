def update_list(numbers, cursor=0):
    current = numbers[cursor]
    if current == 99:
        return

    input1 = numbers[cursor + 1]
    input2 = numbers[cursor + 2]
    output = numbers[cursor + 3]

    if current == 1:
        numbers[output] = numbers[input1] + numbers[input2]
    elif current == 2:
        numbers[output] = numbers[input1] * numbers[input2]
    update_list(numbers, cursor + 4)


def get_output(input1: int, input2: int):
    raw_numbers = raw_numbers_cache.copy()
    raw_numbers[1] = input1
    raw_numbers[2] = input2
    update_list(raw_numbers)
    return raw_numbers[0]


with open('input.txt') as f:
    line = f.readlines()[0].strip()
    raw_numbers_cache = [int(num) for num in line.split(',')]

found = False
value = 0
for noun in range(0, 100):
    for verb in range(0, 100):
        if get_output(noun, verb) == 19690720:
            value = 100 * noun + verb
            found = True
            break
    if found:
        break

print("value: ", value)
