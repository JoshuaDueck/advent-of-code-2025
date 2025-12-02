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


def part1(lines):
    result = 0
    ranges = lines[0].split(',')

    for r in ranges:
        start, end = r.split('-')
        start_int = int(start)
        end_int = int(end)

        for i in range(start_int, end_int+1):
            str_i = str(i)
            if len(str_i) % 2 == 0:
                first_half = str_i[:len(str_i)//2]
                second_half = str_i[len(str_i)//2:]

                if first_half == second_half:
                    result += i
            else:
                continue
    return result


def part2(lines):
    return 0


if __name__ == '__main__':
    main()
