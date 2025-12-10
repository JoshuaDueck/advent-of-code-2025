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


# 833 < X < ???
def part1(lines):
    result = 0
    ranges = []
    ingredients = []
    adding_ranges = True
    for line in lines:
        line = line.strip()
        if line == '':
            adding_ranges = False
        elif adding_ranges:
            ranges.append((int(line.split('-')[0]), int(line.split('-')[1])))
        else:
            ingredients.append(int(line))

    ranges.sort(key=lambda x: x[0])
    i = 0
    while i < len(ranges)-1:
        if ranges[i][1] >= ranges[i+1][0]:
            ranges = delete_and_replace(
                ranges, i, i+1, [(ranges[i][0], ranges[i+1][1])])
            continue
        i += 1

    for ingredient in ingredients:
        for r in ranges:
            if ingredient >= r[0] and ingredient <= r[1]:
                result += 1
                break

    return result


def delete_and_replace(lst, index1, index2, replace_value):
    return lst[:index1] + replace_value + lst[index2+1:]


def part2(lines):
    return 0


if __name__ == '__main__':
    main()
