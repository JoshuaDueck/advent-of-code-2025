import sys
import json
import pdb


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


# We're counting cases where it STARTS at 0, I think? Or rather, cases where
# it starts at 0 and goes negative, or starts at 99 and goes positive...
# We're also missing cases where it starts positive and goes directly to 0?
# Like, if it's 0, 0 // 100 = 0, despite the fact we're pointing at 0.
# 6291 < x < 6408 (not 6354...)
def part2(lines):
    dial_value = 50
    num_zeroes = 0

    for line in lines:
        dial_value, nzc = update_dial2(
            dial_value, line[0], int(line[1:]))

        num_zeroes += nzc if nzc > 0 else 0

    return num_zeroes


def update_dial(curr_dial, direction, value):
    polarity = 1
    if direction == 'L':
        polarity = -1

    full_dial = curr_dial+(value*polarity)
    num_times_past_z = abs(full_dial // 100)

    if full_dial == 0:
        num_times_past_z += 1

    if curr_dial == 0:
        num_times_past_z -= 1

    curr_dial = full_dial % 100
    return (curr_dial, num_times_past_z)


# The issue is that we're counting when it starts at 0 and moving left, and failing to count if it ends at 0 (after a single turn, I think?).
def update_dial2(curr_dial, direction, value):
    polarity = 1
    if direction == 'L':
        polarity = -1

    full_dial = curr_dial+(value*polarity)
    num_times_past_z = abs(full_dial // 100)

    if direction == 'L':
        if curr_dial == 0:
            num_times_past_z -= 1

    curr_dial = full_dial % 100

    if curr_dial == 0 and direction == 'L':
        num_times_past_z += 1

    print(f'The dial is rotated {direction}{value} to point at {
          curr_dial}{f'; during this rotation, it points at 0 {f'{num_times_past_z} times' if num_times_past_z > 1 else 'once'}.' if num_times_past_z > 0 else '.'}')
    return (curr_dial, num_times_past_z)


if __name__ == '__main__':
    main()
