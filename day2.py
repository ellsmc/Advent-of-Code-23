inputdata = []
with open('2_input.txt') as f:
    for line in f.readlines():
        inputdata.append(line)   

max_cubes = {'red': 12, 'blue': 14, 'green': 13}
index = 1
sum = 0

for game in inputdata:
    applicable = []
    game = game.rstrip("\n")
    game = game.replace(";", ",")
    game = game.split(':')
    rounds = game[1]
    cubes = [pair.strip().split() for pair in rounds.split(',')]
    round_max = {}

    for value, colour in cubes:
        value = int(value)
        if colour not in round_max or value > round_max[colour]:
            round_max[colour] = value

    for key in max_cubes:
        if key in round_max:
            if max_cubes[key] >= round_max[key]:
                applicable.append(index)
            else:
                pass
            
    if len(applicable) == 3:
        sum = sum + index
    index += 1

print(sum)
