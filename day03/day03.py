import re  # work with regex patterns

file_name = "input.txt"


def process_input():
    with open(file_name, 'r') as file:
        corrupted_memory = file.read()

    # define valid pattern: mul(X,Y) with X and Y both 1, 2 or 3 digits long
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    # find all matches (tuples of strings)
    matches = re.findall(pattern, corrupted_memory)

    # only keep the integers of the tuples
    valid_multiplications = [(int(x), int(y)) for x, y in matches]

    return valid_multiplications


def sum_of_mul(valid_multiplications):
    return sum(x * y for x, y in valid_multiplications)


def main():
    valid_multiplications = process_input()
    total_sum = sum_of_mul(valid_multiplications)
    print("Sum of valid multiplications:", total_sum)


if __name__ == "__main__":
    main()
