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


# Return lists of least and most values
def least_most_lists(values):
    lcl = [0] * len(values[0])
    mcl = [0] * len(values[0])

    for i in range(0, len(values[0])):
        [lc, mc] = calculate_columns(values, i)
        lcl[i] = str(lc)
        mcl[i] = str(mc)

    return [lcl, mcl]


# Get least and most values from each 'column'
def calculate_columns(values, column):
    temp_list = [values[0][column]]

    for i in range(1, len(values)):
        temp_list.append(values[i][column])

    return least_most_common(temp_list)


def o2_generator_rating(values, index):
    if len(values) == 1:
        return values

    index_list = []

    for value in values:
        index_list.append(value[index])

    [lc, mc] = least_most_common(index_list)

    if lc == mc:
        mc = 1

    matches = []

    # for value in values:
    #     if value[index] == mc:
    #         matches.append(value)
    #     if len(matches) == 0 &

    for i in range(0, len(values)):
        if int(values[i][index]) == int(mc):
            matches.append(value)
        elif len(matches) == 0 and i == len(values) - 1:
            return values[i]

    return o2_generator_rating(matches, index + 1)


def co2_scrubber_rating(values, index):
    if len(values) == 1:
        return values

    index_list = []

    for value in values:
        index_list.append(value[index])

    [lc, mc] = least_most_common(index_list)

    if lc == mc:
        lc = 0

    matches = []

    for i in range(0, len(values)):
        if int(values[i][index]) == int(lc):
            matches.append(value)
        elif len(matches) == 0 and i == len(values) - 1:
            return values[i]

    return o2_generator_rating(matches, index + 1)


# Convert list of 'binary' to decimal
def binary_list_to_decimal(b_list):
    b_num = "".join(b_list)

    return int(b_num, 2)


def main(file_name):
    formatted_inputs = get_formatted_inputs(file_name)
    [lc_list, mc_list] = least_most_lists(formatted_inputs)
    [epsilon_rate, gamma_rate] = [binary_list_to_decimal(
        lc_list), binary_list_to_decimal(mc_list)]
    o2_generator_rating_value = o2_generator_rating(
        formatted_inputs, 0)
    co2_scrubber_rating_value = co2_scrubber_rating(
        formatted_inputs, 0)
    life_support_rating = int(
        o2_generator_rating_value[0], 2) * int(co2_scrubber_rating_value[0], 2)

    print("Epsilon Rate: " + str(epsilon_rate))
    print("Gamma Rate: " + str(gamma_rate))
    print("Power Comsumption: " + str(epsilon_rate * gamma_rate))

    print("O2 Generator Rating: " +
          str(o2_generator_rating_value))
    print("CO2 Scrubber Rating: " +
          str(co2_scrubber_rating_value))
    print("Life Support Rating: " + str(life_support_rating))


main(file_name)
