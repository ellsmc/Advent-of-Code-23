# 12 red cubes, 13 green cubes, and 14 blue cubes
def get_data():
    lines = []
    with open('day2_input.txt') as f:
        for line in f.readlines():
            lines.append(line)   
    return (lines)

print(get_data())