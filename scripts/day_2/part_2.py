from functools import reduce

input_lines: list = open("/Users/vijayk/Programming/aoc-scripts/scripts/day_2/input.txt", "r").readlines()
total: int = 0
valid_configuration: dict = {'red': 12, 'green': 13, 'blue': 14}

while input_lines:
    line: str = input_lines.pop()
    first_split: list = line.split(":") 
    game_id: str = first_split[0][5:]
    configurations: list = first_split[1].split(";")
    flag: bool = True
    min_configuration: dict = {'red': 1, 'green': 1, 'blue': 1}

    for configuration in configurations:
        configuration_split: list = []
        [configuration_split.extend(x.strip().split(" ")) for x in configuration.split(",")]
    
        configuration_dict: dict = dict(zip(
            [color for color in configuration_split if configuration_split.index(color) % 2 != 0],
            [int(value) for value in configuration_split if configuration_split.index(value) % 2 == 0]))
        for color in configuration_dict.keys(): 
            min_configuration[color] = (configuration_dict[color] 
                                       if configuration_dict[color] > min_configuration[color]
                                       else min_configuration[color])

    total += reduce(lambda x, y: x*y, min_configuration.values())

print(f"Total is {total}")