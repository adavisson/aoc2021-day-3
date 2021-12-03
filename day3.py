file_name = "day3-inputs.txt"


# Get formatted_inputs
def get_formatted_inputs(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


# Function to find most and least common in list

# Function to split all inputs into separate lists

print(str(get_formatted_inputs(file_name)))
