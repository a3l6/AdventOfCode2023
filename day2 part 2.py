import re

d2 = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

lines = d2.split("\n")

f = open("day2 part 1.txt", "r")
lines = f.readlines()


def parse_color_string(color_string):
    games = color_string.split(';')
    result_list = []

    for game in games:
        matches = re.findall(r'(\d+) (blue|red|green)', game)
        color_count = {'red': 0, 'green': 0, 'blue': 0}

        for count, color in matches:
            color_count[color] += int(count)

        result_list.append([color_count['red'], color_count['green'] , color_count['blue']])

    return result_list


def find_min_cubes_for_game(game) -> tuple[int, int, int]:
    red = []
    green = []
    blue = []

    for i in range(len(game)):
        red.append(game[i][0])
        green.append(game[i][1])
        blue.append(game[i][2])

    return max(red), max(green), max(blue)


results = []
for game in lines:
    results.append(find_min_cubes_for_game(parse_color_string(game)))

final_result = 0
for game in results:
    final_result += game[0] * game[1] * game[2]

print(final_result)
f.close()