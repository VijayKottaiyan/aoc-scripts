input_lines: list = open("/Users/vijayk/Programming/aoc-scripts/scripts/day_1/input.txt", "r").readlines()
total: int = 0

for line in input_lines:
    list_int: list = [char for char in line if char.isnumeric()]
    num_val: int = int(list_int[0] + list_int[-1]) if len(list_int) > 0 else 0
    total += num_val

print(f"Total is {total}")