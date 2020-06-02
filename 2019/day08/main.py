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


def num_occ(layer: str, number: int):
    return len([n for n in layer if int(n) == number])


def main():
    data = parse()
    width = 25
    height = 6
    layers = get_layers(data, width, height)
    layers_and_0_occ = [(layer, num_occ(layer, 0)) for layer in layers]
    layer_with_less_0 = min(layers_and_0_occ, key=lambda t: t[1])[0]  # min by num of 0 occ
    print("number of 1s * 2s:", num_occ(layer_with_less_0, 1) * num_occ(layer_with_less_0, 2))

    message = ""
    for h in range(0, height):
        for w in range(0, width):
            for layer in layers:
                current = layer[w + width * h]
                if current != "2":
                    message += "0" if current == "1" else " "
                    break
        message += "\n"
    print(message)


if __name__ == "__main__":
    main()
