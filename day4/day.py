import sys
import json


def main():
    with open('custom_cases.json') as f:
        test_cases = json.load(f)
        print('\n\n\n\n\n\n\n\n========== PART 1 ==========')
        for test_case in test_cases['part1']:
            result = part1(test_case['lines'])
            if result == test_case['expected']:
                print(f'\t\033[92m✓ PASS - {test_case['name']}\033[0m')
            else:
                print("\t\033[91m✕ FAIL - {}\
                    \n\t\texpected: {}, actual: {}\033[0m".format(test_case['name'], test_case['expected'], result))

        print('\n========== PART 2 ==========')
        for test_case in test_cases['part2']:
            result = part2(test_case['lines'])
            if result == test_case['expected']:
                print(f'\t\033[92m✓ PASS - {test_case['name']}\033[0m')
            else:
                print("\t\033[91m✕ FAIL - {}\
                    \n\t\texpected: {}, actual: {}\033[0m".format(test_case['name'], test_case['expected'], result))

    if '--test' not in sys.argv:
        with open('input.txt') as f:
            lines = f.readlines()

            print("Part 1:", part1(lines))
            print("Part 2:", part2(lines))


OFFSETS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]


def part1(lines):
    result = 0
    for y, row in enumerate(lines):
        for x, cell in enumerate(row.strip()):
            if cell == '@':
                surrounding_count = 0
                for offset in OFFSETS:
                    o_y = y+offset[0]
                    o_x = x+offset[1]
                    if (o_y >= 0 and o_y < len(lines)) and (o_x >= 0 and o_x < len(row)):
                        if lines[o_y][o_x] == '@':
                            surrounding_count += 1
                if surrounding_count < 4:
                    result += 1
    return result


# Probably my record for the fastest time coding a recursive function ever.
# Whipped it up and it worked first try. And to think that in COMP1020 recursion was the scariest thing to me.
def part2(lines):
    result = 0
    result = get_num_rolls(lines)
    return result


def get_num_rolls(lines):
    print(lines)
    result = 0
    new_lines = []
    for y, row in enumerate(lines):
        new_lines.append('')
        for x, cell in enumerate(row.strip()):
            if cell == '@':
                surrounding_count = 0
                for offset in OFFSETS:
                    o_y = y+offset[0]
                    o_x = x+offset[1]
                    if (o_y >= 0 and o_y < len(lines)) and (o_x >= 0 and o_x < len(row)):
                        if lines[o_y][o_x] == '@':
                            surrounding_count += 1
                if surrounding_count < 4:
                    result += 1
                    new_lines[y] += '.'
                else:
                    new_lines[y] += '@'
            else:
                new_lines[y] += '.'
    if result == 0:
        return result
    else:
        return result + get_num_rolls(new_lines)


if __name__ == '__main__':
    main()
