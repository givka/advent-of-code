import csv
import math


def parse():
    with open('input.txt') as f:
        reader = csv.reader(f)
        first_line = [line for line in reader][0]
        return [char for char in first_line][0]


def fft(number: str, number_phases: int) -> str:
    pattern = [1, 0, -1, 0]
    string = ""
    for p in range(0, number_phases):
        print("p", p, "number", number)

        numbers = [int(c) for c in number]
        string = ""
        for i in range(0, len(number)):
            pattern_repeat = []
            for j in range(i, len(number)):
                index = math.floor((j + 1) / (i + 1)) % (len(pattern))
                pattern_repeat.append(pattern[index - 1])

            value = sum([a * b for a, b in zip(numbers[i:], pattern_repeat)])
            string += str(value)[-1]
        number = string
    return string


def fft_part2(number: str, number_phases: int) -> str:
    number_repeated = ""
    for i in range(0, 10000):
        number_repeated += number

    offset_message = int(number[0:7])
    print("offset_message:", offset_message, "of:", len(number_repeated))

    number_repeated = number_repeated[offset_message:]
    print(len(number_repeated))

    # result = fft(number_repeated, number_phases)
    # return result[offset_message:offset_message + 8]
    pass


def find_digit(number, index):
    n = number[index]

    print("pattern;", index)
    v = len(number) - index

    a = 0
    for i in range(0, v):
        a += int(number[index + i])

    print(str(a)[-1])
    pass


def main():
    number = parse()
    find_digit("12345678", 0)
    find_digit("12345678", 1)
    find_digit("12345678", 2)
    find_digit("12345678", 3)
    find_digit("12345678", 4)
    find_digit("12345678", 5)
    find_digit("12345678", 6)
    find_digit("12345678", 7)
    #assert fft("12345678", 4)[0:8] == "01029498"
    #assert fft("80871224585914546619083218645595", 100)[0:8] == "24176176"
    # assert fft("19617804207202209144916044189917", 100)[0:8] == "73745418"
    # assert fft("69317163492948606335995924319873", 100)[0:8] == "52432133"
    # print('8 first digits:', fft(number, 100)[0:8])

    # fft_part2("03036732577212944063491565474664", 100) == "84462026"
    # fft_part2("02935109699940807407585447034323", 100) == "78725270"
    # fft_part2("03081770884921959731165446850517", 100) == "53553731"

    # fft_part2(number, 100)


if __name__ == "__main__":
    main()
