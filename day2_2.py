inputdata = []
with open('2_input.txt') as f:
    for line in f.readlines():
        inputdata.append(line)   

max_cubes = {'red': 12, 'blue': 14, 'green': 13}
index = 1
sum = 0

for game in inputdata:
    game = game.rstrip("\n")
    game = game.replace(";", ",")
    game = game.split(':')
    rounds = game[1]
    round_max = {}
    cubes = [pair.strip().split() for pair in rounds.split(',')] 

    for value, colour in cubes:
        value = int(value)
        if colour not in round_max or value > round_max[colour]:
            round_max[colour] = value

    power = 1
    for value in round_max.values():
        power *= value
    sum += power
    
print(sum)       
    


