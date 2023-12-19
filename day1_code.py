def text_to_list(filename):
    data_lists = []
    with open(filename, "r") as file:
        for line in file:
            data = line.strip()
            data_lists.append(data)
    return data_lists

print(text_to_list('day1_input.txt'))
