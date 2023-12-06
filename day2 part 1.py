import re

d2 = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

#list_data = d2.split("\n")

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


def check_count_for_game(max_vals: tuple[int, int, int], game_values):
    # check every game
    # ensure that the value in max vals is smaller than the value, if not return true

    # [[4, 3, 0], [1, 6, 2], [0, 0, 2]]

    # repeat length of list times
    for i in range(len(game_values)):
        if game_values[i][0] > max_vals[0]: return False
        if game_values[i][1] > max_vals[1]: return False
        if game_values[i][2] > max_vals[2]: return False

    return True


results = []
for game in lines:
    results.append(parse_color_string(game))

    x = [
        [[4, 3, 0], [1, 6, 2], [0, 0, 2]],
        [[0, 1, 2], [1, 4, 3], [0, 1, 1]],
        [[20, 6, 8], [4, 5, 13], [1, 0, 5]],
        [[3, 6, 1], [6, 0, 3], [14, 15, 3]],
        [[6, 1, 3], [1, 2, 2]]
    ]


final = 0
for game in results:
    valid = check_count_for_game((12, 13, 14), game)
    if valid:
        final += results.index(game) + 1

print(final)

f.close()