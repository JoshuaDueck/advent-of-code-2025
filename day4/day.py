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
        row_cell_counts = []
        for x, cell in enumerate(row.strip()):
            cell_count = 0
            if cell == '@':
                surrounding_count = 0
                for offset in OFFSETS:
                    try:
                        offset_val = lines[y+offset[0]][x+offset[1]]
                        if offset_val == '@':
                            surrounding_count += 1
                    except IndexError:
                        pass
                if surrounding_count < 4:
                    result += 1
                cell_count = surrounding_count
            row_cell_counts.append(cell_count)
        print(''.join([str(i) for i in row_cell_counts]))
    return result


def part2(lines):
    return 0


if __name__ == '__main__':
    main()
