import re  # work with regex patterns

file_name = "input.txt"

# define valid pattern: mul(X,Y) with X and Y both 1, 2 or 3 digits long
mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

with open(file_name, 'r') as file:
    corrupted_memory = file.read()


def process_input():
    # find all matches (tuples of strings)
    matches = re.findall(mul_pattern, corrupted_memory)

    # only keep the integers of the tuples
    valid_multiplications = [(int(x), int(y)) for x, y in matches]

    return valid_multiplications


def sum_of_mul(valid_multiplications):
    return sum(x * y for x, y in valid_multiplications)


def process_enabled_input():
    # multiplication is enabled initially
    mul_enabled = True

    # track enabled and valid multiplications
    enabled = []

    index = 0
    while index < len(corrupted_memory):
        # check if substring matches the do()-instruction
        if re.match(do_pattern, corrupted_memory[index:]):
            mul_enabled = True # in case it had been disabled beforehand
            index += len("do()") # skip past the length of do()
        elif re.match(dont_pattern, corrupted_memory[index:]):
            mul_enabled = False
            index += len("don't()")
        # check if substring matches mul(X,Y) pattern
        elif match := re.match(mul_pattern, corrupted_memory[index:]):
            if mul_enabled: # if matches, still only extract if it fits the do()-instruction
                x, y = map(int, match.groups())
                enabled.append((x, y))
            index += match.end() # if it has don't()-instruction: skip past the matched instruction
        else:
            index += 1 # default: move forward step-by-step if neither do(), don't() or mul(X,Y) is found

    return enabled


def main():
    # task 1
    valid_multiplications = process_input()
    total_sum = sum_of_mul(valid_multiplications)
    print("Sum of valid multiplications:", total_sum)

    # task 2
    enabled_multiplications = process_enabled_input()
    enabled_sum = sum_of_mul(enabled_multiplications)
    print("Sum of enabled only multiplications:", enabled_sum)


if __name__ == "__main__":
    main()
