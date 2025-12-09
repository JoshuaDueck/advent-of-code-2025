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
    for bank in lines:
        largest_battery = int(bank[0])
        largest_index = 0
        bank = bank.strip()
        for i in range(len(bank)-1):
            if int(bank[i]) > largest_battery:
                largest_battery = int(bank[i])
                largest_index = i

        second_largest_b = int(bank[largest_index+1])
        for i in range(largest_index+1, len(bank)):
            if int(bank[i]) > second_largest_b:
                second_largest_b = int(bank[i])

        result += int(str(largest_battery)+str(second_largest_b))

    return result


NUM = 12


# I CANNOT BELIEVE I DID IT
# THE ALGO WAS SOUND, I JUST NEEDED TO EXECUTE
# Wait hold on, I fail all my test cases lol, I have no clue how I passed the actual case...
# That's going to upset me for a while...
def part2(lines):
    result = 0
    for bank in lines:
        bank_stack = []
        bank = bank.strip()
        for i, batt in enumerate(bank):
            while len(bank_stack) > 0 \
                and bank_stack[-1] < int(batt) \
                    and (len(bank_stack) + len(bank)-i) > NUM:  # LOL OKAY I LITERALLY WAS NOT CHECKING THE .STRIPPED VERSION HERE AAUGH
                bank_stack.pop()
            bank_stack.append(int(batt))

        bank_stack = bank_stack[:NUM]

        bank_str = ''.join([str(i) for i in bank_stack])
        print(bank_str)
        result += int(bank_str)

    return result


def find_all_indices(s, search):
    return [i for i, x in enumerate(s) if x == search]


if __name__ == '__main__':
    main()
