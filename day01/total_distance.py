file_name = "input01.txt"


def process_input():
    # add numbers from the left side to a list and do the same with the right side
    left_numbers = []
    right_numbers = []

    with open(file_name, 'r') as file:
        for line in file:
            # split the line into two numbers and add them to their respective lists
            try:
                left, right = map(int, line.split())
                left_numbers.append(left)
                right_numbers.append(right)
            except ValueError:
                print("Value Error.")

    # return sorted number lists
    return sorted(left_numbers), sorted(right_numbers)


def calculate_total_distance():
    left_numbers, right_numbers = process_input()
    # zip creates pairs based on the index, then get the result of the abs subtraction and returns it
    return sum([abs(left - right) for left, right in zip(left_numbers, right_numbers)])


def main():
    total = calculate_total_distance()
    print("total:", total)


if __name__ == "__main__":
    main()
