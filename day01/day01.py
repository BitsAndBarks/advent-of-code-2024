from collections import Counter

file_name = "input.txt"


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


def calculate_total_distance(left_numbers, right_numbers):
    # zip creates pairs based on the index, then get the result of the abs subtraction and returns it
    return sum([abs(left - right) for left, right in zip(left_numbers, right_numbers)])


def calculate_similarity_score(left_numbers, right_numbers):
    # counts occurrences in the right list
    right_count = Counter(right_numbers)

    score = 0
    for number in left_numbers:
        score += number * right_count.get(number, 0) # multiply by no. of appearances, and by 0 if only in left list

    return score

def main():
    left, right = process_input()
    distance = calculate_total_distance(left, right)
    similarity = calculate_similarity_score(left, right)
    print("total:", distance)
    print("similarity:", similarity)


if __name__ == "__main__":
    main()
