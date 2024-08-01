import re
import math


def solution_part_one(puzzle_string):
    # get numbers out off input string
    x = list(map(int, re.findall("\d+", puzzle_string)))
    split_index = len(x) // 2

    beat_the_records = [
        sum(1 for j in range(x[i]) if x[i + split_index] < j * (x[i] - j))
        for i in range(0, split_index)
    ]

    return math.prod(beat_the_records)


def solution_part_two(puzzle_string):
    x: list = re.findall("\d+", puzzle_string)
    split_index: int = len(x) // 2
    time: int = int("".join(x[:split_index]))
    distance: int = int("".join(x[split_index:]))

    low_barrier, high_barrier = next((i for i in range(0, time) if distance < i * (time - i)), None), next(
        (i for i in range(time, 0, -1) if distance < i * (time - i)), None)

    return high_barrier - (low_barrier) + 1


if __name__ == '__main__':
    with open('./input/Day6_1.txt', 'r') as f:
        puzzle_input = f.read()

    #print(solution_part_one(puzzle_input))
    print(solution_part_two(puzzle_input))
