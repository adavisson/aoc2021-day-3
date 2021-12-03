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
        if int(value) == 0:
            zero_count += 1
        elif int(value) == 1:
            one_count += 1

    return [0, 1] if zero_count < one_count else [1, 0]


# Function to split all inputs into separate lists
def split_into_lists(values):
    lists = [[int(value)] for value in values[0]]
    print(lists)

    return lists


print(str(split_into_lists(get_formatted_inputs(file_name)))[0])
