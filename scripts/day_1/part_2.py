input_lines: list = open("/Users/vijayk/Programming/aoc-scripts/scripts/day_1/input.txt", "r").readlines()
total: int = 0

mappings: dict = {
    '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'one': 1, 'two': 1, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven' : 7, 'eight' : 8, 'nine': 9
}

for line in input_lines:
    list_int: list = [] 
    for char_pos in range(0, len(line) - 1):
        char1: str = line[char_pos] 
        char2: str = line[char_pos+1]
        word_beg: str = char1 + char2 if(not char1.isnumeric() and not char2.isnumeric()) \
                                      else char1 if char1.isnumeric() else char2
        key: str = [key for key in mappings.keys() if key.startswith(word_beg)]
        key = key[0] if len (key) == 1 else 'empty'
        substring: str = line[char_pos: char_pos+len(key)]
        if substring == key: list_int.append(mappings[key])
    
    num_val: int = (list_int[0] * 10) + list_int[-1] if len(list_int) > 0 else 0
    total += num_val

print(f"Total is {total}")