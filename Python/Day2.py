import re

import numpy
import numpy as np

dice_cup_dict:  dict = {"green": 13, "red": 12, "blue": 14}

def solution_first_task(lst:list):

    valid_games_list: list = []
    for game in lst:

        x = game.replace("Game", "").strip().split(":")
        if game_check(x[1]):
            valid_games_list.append(int(x[0]))


    return sum(valid_games_list)

def game_check(game_state_list: str) -> bool:
    for color in ["blue", "green", "red"]:

        if max([int(m) for m in re.findall(f"(\d+) {color}", game_state_list)]) > dice_cup_dict[color]:
            return False

    return True

def game_check_two(game_state_list: str) -> bool:
    power_list = []
    for color in ["blue", "green", "red"]:

        power_list.append(max([int(m) for m in re.findall(f"(\d+) {color}", game_state_list)]))

    return numpy.prod(power_list)

def solution_seccond_task(lst: list):

    valid_games_list: list = []
    for game in lst:

        x = game.replace("Game", "").strip().split(":")
        valid_games_list.append(game_check_two(x[1]))


    return sum(valid_games_list)



def open_read_file(filename: str):

    with open(filename, "r") as f:
        lines = f.readlines()
    return lines


if __name__ == '__main__':
    content_file_list: list = open_read_file("./input/day2_1.txt")

    test_list = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
    print(solution_seccond_task(content_file_list))