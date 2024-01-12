import re

def text_to_list(filename):
    data_lists = []
    with open(filename, "r") as file:
        for line in file:
            data = line.strip()
            data_lists.append(data)
    return data_lists

# do i need to split the  large integers into digits?
def extract_numbers(item):
    numbers = re.findall('[0-9]+', item)
    numbers = [int(element) for element in numbers]
    return numbers

def calculate_calibration(numbers_list):
    list_to_add = []
    for sublist in numbers_list:
        if len(sublist) == 1 and len(str(sublist[0])) == 1:
            list_to_add.append(int(str(sublist[0]) * 2))
        elif len(sublist) == 1 and len(str(sublist[0])) == 2:
            list_to_add.append(int(str(sublist[0])))
        elif len(sublist) > 1:
            list_to_add.append(int(str(sublist[0]) + str(sublist[-1])))
    return list_to_add

### sum of smaller day 1 should be 408 ###
calibration_values = []
for entry in text_to_list('smallerday1.txt'):
    calibration_values.append(extract_numbers(entry))

print(calibration_values)
print(calculate_calibration(calibration_values))