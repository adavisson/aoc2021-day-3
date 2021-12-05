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


# Get column using index
def get_column(values, index):
    column = map(lambda x: x[index], values)

    return list(column)


# Return lists of least and most values
def least_most_lists(values):
    lcl = [0] * len(values[0])
    mcl = [0] * len(values[0])

    for i in range(0, len(values[0])):
        column = get_column(values, i)
        [lc, mc] = least_most_common(column)
        lcl[i] = str(lc)
        mcl[i] = str(mc)

    return [lcl, mcl]


# Convert list of 'binary' to decimal
def binary_list_to_decimal(b_list):
    b_num = "".join(b_list)

    return int(b_num, 2)


def o2_generator_rating(values, index, common_values):
    if (len(values) == 1):
        return values

    matches = []

    for i in range(0, len(values)-1):
        if values[i][index] == common_values[index]:
            matches.append(values[i])

    if len(matches) < 1:
        return [values[len(values) - 1]]

    return o2_generator_rating(matches, index + 1, common_values)


def main(file_name):
    formatted_inputs = get_formatted_inputs(file_name)
    [lc_list, mc_list] = least_most_lists(formatted_inputs)
    [epsilon_rate, gamma_rate] = [binary_list_to_decimal(
        lc_list), binary_list_to_decimal(mc_list)]

    o2 = o2_generator_rating(formatted_inputs, 0, mc_list)
    co2 = o2_generator_rating(formatted_inputs, 0, lc_list)
    life_support_rating = int(o2[0], 2) * int(co2[0], 2)

    print("Epsilon Rate: " + str(epsilon_rate))
    print("Gamma Rate: " + str(gamma_rate))
    print("Power Comsumption: " + str(epsilon_rate * gamma_rate))

    print("Oxygen Generator Rating: " + str(o2))
    print("CO2 Scrubber Rating: " + str(co2))
    print("Life Support Rating: " + str(life_support_rating))


main(file_name)
