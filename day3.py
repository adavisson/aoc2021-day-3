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


def least_most_lists(values):
    lcl = [0] * len(values[0])
    mcl = [0] * len(values[0])

    for i in range(0, len(values[0])):
        [lc, mc] = calculate_columns(values, i)
        lcl[i] = str(lc)
        mcl[i] = str(mc)

    return [lcl, mcl]


def calculate_columns(values, column):
    temp_list = [values[0][column]]

    for i in range(1, len(values)):
        temp_list.append(values[i][column])

    return least_most_common(temp_list)


def binary_list_to_decimal(b_list):
    b_num = "".join(b_list)

    return int(b_num, 2)


def main(file_name):
    formatted_inputs = get_formatted_inputs(file_name)
    [lc_list, mc_list] = least_most_lists(formatted_inputs)
    [epsilon_rate, gamma_rate] = [binary_list_to_decimal(
        lc_list), binary_list_to_decimal(mc_list)]

    print("Epsilon Rate: " + str(epsilon_rate))
    print("Gamma Rate: " + str(gamma_rate))
    print("Power Comsumption: " + str(epsilon_rate * gamma_rate))


main(file_name)
