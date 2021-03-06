def parse():
    with open('input.txt') as f:
        return [line.strip().split(')') for line in f.readlines()]


class Planet:
    def __init__(self, name, parent: 'Planet'):
        self.name = name
        self.parent = parent
        self.children = []

    def __str__(self):
        return f"({self.name}: parent->{self.parent})"

    def number_of_orbits(self):
        number = 0
        parent = self.parent
        while parent is not None:
            number += 1
            parent = parent.parent
        return number

    def check_if_parent_has_name(self, name, last_name="", step=0, results=[]):
        step += 1

        look_for = self.children.copy()
        look_for.append(self.parent)
        look_for = [look for look in look_for if look and look.name != last_name]

        for look in look_for:
            if look.name == name:
                results.append(step - 2)  # remove origin and destination
            look.check_if_parent_has_name(name, self.name, step, results)

        return results


def fill_planet_dict(planets):
    planets_dict = {}
    for planet in planets:
        first_name = planet[0]
        second_name = planet[1]
        if (first_name in planets_dict) is False:
            planets_dict[first_name] = Planet(first_name, None)
        if (second_name in planets_dict) is False:
            planets_dict[second_name] = Planet(second_name, None)

        parent = planets_dict[first_name]
        planets_dict[second_name].parent = parent
        parent.children.append(planets_dict[second_name])
    return planets_dict


def main():
    planets = parse()
    planets_dict = fill_planet_dict(planets)

    number_of_orbits = [planets_dict[key].number_of_orbits() for key in planets_dict]
    print("number of orbits:", sum(number_of_orbits))
    number_of_connections = planets_dict['YOU'].check_if_parent_has_name('SAN')
    print("number of connections:", min(number_of_connections))


if __name__ == "__main__":
    main()
