input_lines: list = open("/Users/vijayk/Programming/aoc-scripts/scripts/day_2/input.txt", "r").readlines()
total: int = 0
valid_configuration: dict = {'red': 12, 'green': 13, 'blue': 14}

while input_lines:
    line: str = input_lines.pop()
    first_split: list = line.split(":") 
    game_id: str = first_split[0][5:]
    configurations: list = first_split[1].split(";")
    flag: bool = True

    for configuration in configurations:
        configuration_split: list = []
        [configuration_split.extend(x.strip().split(" ")) for x in configuration.split(",")]
    
        configuration_dict: dict = dict(zip(
            [color for color in configuration_split if configuration_split.index(color) % 2 != 0],
            [int(value) for value in configuration_split if configuration_split.index(value) % 2 == 0]))
        
        configuration_check: list = [True if configuration_dict[color] <= valid_configuration[color]
                                    else False
                                    for color in configuration_dict.keys()]
        
        flag = True if False not in configuration_check else False 
        if not flag: break
    
    total += int(game_id) if flag else 0

print(f"Total is {total}")