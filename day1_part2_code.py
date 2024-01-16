word_to_number = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

import re

def extract_numbers(string_list):
    numeric_result = []
    textual_result = []

    for inner_list in string_list:
        for string in inner_list:
            # Extract numeric representations
            numeric_matches = re.findall(r'\d+', string)
            numeric_result.extend(map(int, numeric_matches))

            # Extract textual representations
            textual_matches = re.findall(r'[a-zA-Z]+', string)
            textual_result.extend(textual_matches)

    return numeric_result, textual_result

# Example usage
input_strings = [['two1nine'], ['eightwothree'], ['abcone2threexyz'], ['xtwone3four'], ['4nineeightseven2'], ['zoneight234'], ['7pqrstsixteen']]
numeric_numbers, textual_numbers = extract_numbers(input_strings)

print("Numeric representations:", numeric_numbers)
print("Textual representations:", textual_numbers)