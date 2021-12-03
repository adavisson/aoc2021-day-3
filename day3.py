file_name = "day3-inputs.txt"


# Get formatted_inputs
def get_formatted_inputs(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


# Function to find most and least common in list
# Assumes list of 0's and 1's
def least_most_common(values):
    zero_count = 0
    one_count = 0

    for value in values:
        if value == "0":
            zero_count += 1
        elif value == "1":
            one_count += 1

    return [0, 1] if zero_count < one_count else [1, 0]


# Function to split all inputs into separate lists
def split_into_lists(values):
    lists = [[0] * len(values)] * len(values[0])

    for i in range(0, len(values)):
        for j in range(0, len(values[i])):
            lists[j][i] = values[i][j]

    return lists


# Function to return list of least common and most common values
def least_most_common_lists(lists):
    least_common = [0] * len(lists)
    most_common = [0] * len(lists)

    print(lists)
    for i in range(0, len(lists)):
        [lc, mc] = least_most_common(lists[i])
        least_common[i] = lc
        most_common[i] = mc

        i += 1
    return [least_common, most_common]


print(str(least_most_common_lists(split_into_lists(get_formatted_inputs(file_name)))))
