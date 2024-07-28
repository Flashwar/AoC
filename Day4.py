import re
import ast
def open_read_file(filename: str) -> list:
    with open(filename, "r") as f:
        lines = f.readlines()
        #lines = re.sub("Card\s+\d+:", "", lines)
    return [line.replace("\n", "") for line in lines]

def part_1(Puzzleinput: list) -> int:

    ticket_points_sum = 0
    for line in Puzzleinput:
        winning_numbers,own_numbers = re.sub("\s+",",", re.sub("\s\|\s+", "|", re.sub("Card\s+\d+:\s+", "", line))).split('|')
        ticket_points_sum +=2 ** (len(set(ast.literal_eval(own_numbers)).intersection(set(ast.literal_eval(winning_numbers))))-1) if len(set(ast.literal_eval(own_numbers)).intersection(set(ast.literal_eval(winning_numbers))))-1 >= 0 else 0

    return ticket_points_sum

def part_2(Puzzleinput:list)-> int:

    store_dict = {key:1 for key in range(len(Puzzleinput))}

    for ident,line in enumerate(Puzzleinput):
        winning_numbers, own_numbers = re.sub("\s+", ",",
                                              re.sub("\s\|\s+", "|", re.sub("Card\s+\d+:\s+", "", line))).split('|')
        for x in range(1, len(set(ast.literal_eval(own_numbers)).intersection(set(ast.literal_eval(winning_numbers))))+ 1):
            store_dict[ident+x]+=1*store_dict[ident]
    print(store_dict)
    return sum(store_dict.values())

if __name__ == '__main__':
    puzzle_input = open_read_file("./input/Day4_input.txt")
    x =part_2(puzzle_input)
    print(x)
