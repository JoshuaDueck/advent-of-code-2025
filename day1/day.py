import sys
import json


def main():
    with open('custom_cases.json') as f:
        test_cases = json.load(f)
        print('========== PART 1 ==========')
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


def part1(lines):
    curr = 50
    num_zeroes = 0

    for line in lines:
        sign = 1
        direction = line[0]
        value = int(line[1:])

        if direction == 'L':
            sign = -1

        curr = (curr+(sign*value)) % 100

        if curr == 0:
            num_zeroes += 1

    return num_zeroes


# Doesn't account for rotations > 100 positions.
# Will need to get the number, negative or positive
# Doing value % 100 gives us the correct value
# The size of the value pre-mod will give us the number of times crossing 0 (?)
# 6291 < x < 6408 (not 6354...)
def part2(lines):
    dial_value = 50
    num_zeroes = 0

    for line in lines:
        sign = 1
        direction = line[0]
        value = int(line[1:])

        if direction == 'L':
            sign = -1

        theoretical_value = (dial_value+(sign*value))
        dial_value = theoretical_value % 100

        num_times_crossing_zero = 0
        if theoretical_value < 0:
            num_times_crossing_zero = abs(theoretical_value // 99)
        else:
            num_times_crossing_zero = abs(theoretical_value // 100)
        num_zeroes += num_times_crossing_zero

    return num_zeroes


if __name__ == '__main__':
    main()
