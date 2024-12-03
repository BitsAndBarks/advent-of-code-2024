file_name = "input.txt"


def process_input():
    levels = []

    with open(file_name, 'r') as file:
        for line in file:
            try:
                level = list(map(int, line.split()))
                levels.append(level)
            except ValueError:
                print("Value Error.")

    return levels


def is_increasing(level):
    for i in range(1, len(level)):
        if not (1 <= level[i] - level[i - 1] <= 3):
            return False
    return True


def is_decreasing(level):
    for i in range(1, len(level)):
        if not (-3 <= level[i] - level[i - 1] <= -1):
            return False
    return True


def is_safe_with_dampener(level):
    for i in range(len(level)):
        # remove current entry to check if level becomes safe
        modified_level = level[:i] + level[i + 1:]
        if is_increasing(modified_level) or is_decreasing(modified_level):
            return True
    return False


def calculate_safe_levels(all_levels):
    safe = 0

    for levels in all_levels:
        # determine if numbers should go up or down
        trend = levels[1] - levels[0]
        if 1 <= trend <= 3:  # must increase
            if is_increasing(levels):
                safe += 1
        elif -3 <= trend <= -1:  # must decrease
            if is_decreasing(levels):
                safe += 1

    return safe


def calculate_with_dampener(all_levels):
    safe = 0

    for levels in all_levels:
        # no need to check trend first as it may be safe with dampener
        if is_increasing(levels) or is_decreasing(levels):
            safe += 1
        else:
            # call dampener only in case we need to do another check
            if is_safe_with_dampener(levels):
                safe += 1

    return safe


def main():
    all_levels = process_input()
    safe_levels = calculate_safe_levels(all_levels)
    print("Safe levels:", safe_levels)
    safe_with_dampener = calculate_with_dampener(all_levels)
    print("Safe levels with dampener:", safe_with_dampener)


if __name__ == "__main__":
    main()
