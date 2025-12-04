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


# Find largest number before index len(bank)-12
# "What is the largest number we can make with the remaining chunk?
# It could be a recursive problem?
# Params: chunk to get largest from
# Returns: largest concatenated number in the group
# 818181911112111
#
# Or, we start with the last N highlighted.
# The lowest index one gets incremented to find the largest of all previous numbers (and chooses the furthest back one)
# Then, we go to the next lowest index and do the same thing, stopping before the previous one.
# At each step, the number we create must be the largest up until that point.

# Let's say for the largest with 3:
# i.e. [8889] [11112111]
#   181911112111
#
# I mean, this is litearlly just kind of the work from the end method...
# Just work from the end back, finding the largest number with index <= len(bank)-i
#
# Can we just go through once? I.e. keep track of the N largest numbers in a row we pass on the way to the end?
# The trickiest part is the fact that the numbers need to be in order, right?
# Maybe it's not actually tricky, since we're going in reverse order? All we need to do is check >=
# Store tuples in the list?
# For every candidate we encounter, if it's larger than the curr head, new curr head, otherwise check if it's larger than or equal to the next largest, if not, remain.
# 818[181911112111]
# ..^..............
# The problem with that approach is that whenever we update one index to the next, we also need to update the next index to the NEXT.
# We'll need a more clever solution, I don't know if we can beat O(n*m) where n is number of entries and m is number of digits.
# I think technically, we could just find all instances of each digit.
# It would technically be linear time lol, since 10 digits is a constant :P Idk if that's how it works.
# Then we literally just go through the whole array 10 times. Effectively, find as many 9s as possible up to 12, OR until we have no space for the rest at the end (which changes depending on how many we've found).
# Once we find this, find the furthest 9 without going over, and search 8s in that cluster in the same way.
# The thing is, we can still use 9s in the last 12 digits of the bank, just not as first indices. This makes it really hard to successfully do this, without some other data structure.

# Okay, perhaps we use a stack? Add every entry to the stack, unless we hit a higher one?
# When we hit a number higher than one earlier, pop to that number (store the highest index and value in the stack)
# The only thing is, we need to leave room at the end. That is, if there's not enough numbers to choose from, don't pop anything.
NUM = 12


def part2(lines):
    result = 0
    # 98855    <-7
    for bank in lines:
        bank_stack = [int(bank[0])]
        for batt, i in enumerate(bank[:-NUM]):
            while len(bank_stack) > 0 and int(batt) > bank_stack[-1]:
                bank_stack = bank_stack[:-1]
            bank_stack.append(int(batt))

        if len(bank_stack) < NUM:
            bank_stack.append(bank[-NUM:])

        bank_stack = bank_stack[:NUM]

        bank_str = ""
        for val in bank_stack:
            bank_str += str(val)

        print('Highest is:', bank_str)
        result += int(bank_str)

    return result


def find_all_indices(s, search):
    return [i for i, x in enumerate(s) if x == search]


if __name__ == '__main__':
    main()
