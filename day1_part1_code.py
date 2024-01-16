import re

def text_to_list(filename):
    data_lists = []
    with open(filename, "r") as file:
        for line in file:
            data = line.strip()
            data_lists.append(data)
    return data_lists

def extract_numbers(item):
    numbers = re.findall('[0-9]+', item)
    numbers = [int(element) for element in numbers]
    return numbers

def seperate_to_digits(numbers):
    single_digits = []
    for sublist in numbers:
        modifier = []
        for num in sublist:
            modifier.extend([int(digit) for digit in str(num)])
        single_digits.append(modifier)
    return single_digits

def first_and_last(numbers):
    list_to_add = []
    for sublist in numbers:
        if len(sublist) == 1 and len(str(sublist[0])) == 1:
            list_to_add.append(int(str(sublist[0]) * 2))
        elif len(sublist) == 1 and len(str(sublist[0])) == 2:
            list_to_add.append(int(str(sublist[0])))
        elif len(sublist) > 1:
            list_to_add.append(int(str(sublist[0]) + str(sublist[-1])))
    return list_to_add

def sum_of_list(numbers):
    total = 0
    for element in numbers:
        total+= element
    return total

calibration_values = []
for entry in text_to_list('day1_input.txt'):
    calibration_values.append(extract_numbers(entry))
digitised_calibrations = seperate_to_digits(calibration_values)
add_me = first_and_last(digitised_calibrations)
total_calibration = sum_of_list(add_me)
print("Sum of all integers:", total_calibration)