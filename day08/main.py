import csv


def parse():
    with open('input.txt') as f:
        reader = csv.reader(f)
        return [line for line in reader][0][0]


def get_layers(data: str, width: int, height: int):
    layers = []
    cursor = 0
    while cursor != len(data):
        layers.append(data[cursor: cursor + width * height])
        cursor += width * height
    return layers


def get_number_occ(layer: str, number: int):
    return len([n for n in layer if int(n) == number])


def main():
    data = parse()
    layers = get_layers(data, 25, 6)
    layers_and_0_occ = [(layer, get_number_occ(layer, 0)) for layer in layers]
    layer_with_less_0 = min(layers_and_0_occ, key=lambda t: t[1])[0]
    print("number of 1s by 2s:", get_number_occ(layer_with_less_0, 1) * get_number_occ(layer_with_less_0, 2))


if __name__ == "__main__":
    main()
