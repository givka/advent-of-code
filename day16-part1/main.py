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
        numbers = [int(c) for c in number]
        string = ""
        for i in range(0, len(number)):
            pattern_repeat = []
            for j in range(0, len(number)):
                index = math.floor((j + 1) / (i + 1)) % (len(pattern))
                pattern_repeat.append(pattern[index - 1])
            value = sum([a * b for a, b in zip(numbers, pattern_repeat)])
            string += str(value)[-1]
        number = string
    return string[0:8]


def main():
    number = parse()
    assert fft("12345678", 4) == "01029498"
    assert fft("80871224585914546619083218645595", 100) == "24176176"
    assert fft("19617804207202209144916044189917", 100) == "73745418"
    assert fft("69317163492948606335995924319873", 100) == "52432133"
    print('8 first digits:', fft(number, 100))


if __name__ == "__main__":
    main()
