from day1_part1_code import first_and_last, sum_of_list

def get_data():
    lines = []
    with open('day1_input.txt') as f:
        for line in f.readlines():
            lines.append(line)   
    return (lines)

def calculate_calibration2(data_noise):
        word_to_digit = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
        digit_list = []
        for line in data_noise:
            # := walrus operator - assignment on condition
            converted_words = [convert if (convert := "".join([number for word, number in word_to_digit.items() if line[index:].startswith(word)])) else line[index] for index in range(len(line))]
            digits = [int(i) for i in converted_words if i.isdigit()]
            digit_list.append(digits)
        return digit_list

print("Sum total part two: ", sum_of_list(first_and_last(calculate_calibration2(get_data()))))