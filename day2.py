# 12 red cubes, 13 green cubes, and 14 blue cubes
def get_data():
    lines = []
    with open('2_input.txt') as f:
        for line in f.readlines():
            lines.append(line)   
    return (lines)

def find_highest_counts(game_data):
    colour_counts = {}    
    for game in game_data:
        game_parts = game.split(':')
        game_number = game_parts[0].strip()
        counts_str = game_parts[1].strip()
        print(game_number)
        counts_list = counts_str.split(';')
        for count_set in counts_list:
            colours = count_set.split(',')
            print(colours) # here I have the games and the rounds individually
            for colour in colours:
                colour_count = colour.strip().split()
                colour_name = colour_count[1]
                count = int(colour_count[0])
                print(colour_name, count)
                for i in game:
                    i = 1
                if colour_name not in colour_counts or count > colour_counts[colour_name]:
                    colour_counts[colour_name] = count
    return colour_counts

fulldata = get_data()
result = find_highest_counts(fulldata)

for colour, count in result.items():
    print(f'highest count of {colour}: {count}')



