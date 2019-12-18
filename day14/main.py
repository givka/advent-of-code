import math


def parse():
    with open('input.txt') as f:
        d = {}
        for line in f.readlines():
            inputs, output = line.strip().split('=>')
            inputs = inputs.split(',')
            inputs = [i.strip().split(' ') for i in inputs]
            output = output.strip().split(' ')

            output = Reaction(output[1], int(output[0]), [(i[1], int(i[0])) for i in inputs])
            d[output.name] = output

        return d


class Reaction:
    def __init__(self, name: str, number: int, inputs: list):
        self.name = name
        self.number = number
        self.inputs = inputs
        self.raw = inputs[0][0] == "ORE"

    def __repr__(self):
        return f"Reaction({self.name})"

    def get_raw(self, reactions, counters, stash):
        for i in self.inputs:
            name, number = i
            reaction = reactions[name]
            if reaction.raw:
                counters[reaction.name] += number
            else:
                count = 0
                while count < number:
                    if stash[reaction.name] >= reaction.number:
                        print(True)
                        stash[reaction.name] -= reaction.number
                    else:
                        reaction.get_raw(reactions, counters, stash)
                    count += reaction.number
                stash[reaction.name] = count - number
                print(stash)


def get_ore_from_stash(reactions: dict, stash: dict):
    count = 0
    for name in stash:
        reaction = reactions[name]
        number_raw = stash[name]
        number_to_craft = math.ceil(number_raw / reaction.number)
        count += number_to_craft * reaction.inputs[0][1]
    return count


def main():
    reactions = parse()

    counters = {}
    stash = {}
    for r in reactions:
        if reactions[r].raw:
            counters[r] = 0
        stash[r] = 0

    reactions['FUEL'].get_raw(reactions, counters, stash)
    print(counters)
    print("ore needed:", get_ore_from_stash(reactions, counters))


if __name__ == "__main__":
    main()
