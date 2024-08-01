import re
from itertools import product


def open_read_file(filename: str) -> list:
    with open(filename, "r") as f:
        lines = f.readlines()
    return [line.replace("\n", "") for line in lines]


def get_indexs_values_numbers(lines: list) -> list:
    return_list: list = []
    for ident, line in enumerate(lines):

        matches_list: list = []
        for match in re.finditer("\d+", line):
            matches_list.append((ident, match.start(), match.end(), int(match.group())))

        return_list.append(matches_list)

    return return_list


def check_position(lines: list, vertical, horizontal) -> bool:
    if lines[vertical][horizontal].isdigit():
        return True

def get_indexes_symbols(lines: list) -> list:
    return [(ident, pos_symbol) for ident, line in enumerate(lines) for pos_symbol, symbol in enumerate(line) if
            not symbol.isdigit() and symbol != "."]

def get_indexes_asterixs(lines: list) -> list:
    return [(ident, pos_symbol) for ident, line in enumerate(lines) for pos_symbol, symbol in enumerate(line) if
            not symbol.isdigit() and symbol == "*"]

def get_values(number_list: list, vertical, horizontal) -> int:
    for x in number_list[vertical]:

        if x[1] <= horizontal <= x[2]:
            return x[3]


def check_if_element_horizontally_vertically_diagonal(lines: list):
    kartesian_product_list: list = list(product([-1, 0, +1], [-1, 0, +1]))

    index_elements = get_indexs_values_numbers(lines)
    print(index_elements)
    pos_symbol_list: list = get_indexes_symbols(lines)
    print(pos_symbol_list)

    return_list = []
    for symbol_line, pos_symbol in pos_symbol_list:
        value_list = [[],[],[]]
        try:
            for vertical_add, horizontal_add in kartesian_product_list:
                if lines[symbol_line + vertical_add][pos_symbol + horizontal_add].isdigit() and (
                        vertical_add != 0 or horizontal_add != 0):
                    value = get_values(index_elements, symbol_line + vertical_add, pos_symbol + horizontal_add)
                    if value not in value_list[vertical_add]:
                        value_list[vertical_add].append(value)
        except IndexError:
            pass
        return_list.extend([z for x in value_list for z in x])

    print(return_list)
    return sum(return_list)


def get_gear_with_two_part_numbers(lines: list):
    kartesian_product_list: list = list(product([-1, 0, +1], [-1, 0, +1]))

    index_elements = get_indexs_values_numbers(lines)
    print(index_elements)
    pos_symbol_list: list = get_indexes_asterixs(lines)
    print(pos_symbol_list)

    return_list = []
    for symbol_line, pos_symbol in pos_symbol_list:
        value_list = [[],[],[]]
        try:
            for vertical_add, horizontal_add in kartesian_product_list:
                if lines[symbol_line + vertical_add][pos_symbol + horizontal_add].isdigit() and (
                        vertical_add != 0 or horizontal_add != 0):
                    value = get_values(index_elements, symbol_line + vertical_add, pos_symbol + horizontal_add)
                    if value not in value_list[vertical_add]:
                        value_list[vertical_add].append(value)
        except IndexError:
            pass

        if len(z:=[z for x in value_list for z in x]) == 2:
            return_list.append(z[0]*z[1])

    print(return_list)
    return sum(return_list)


if __name__ == '__main__':
    content_file_list: list = open_read_file("./input/Day3_1.txt")
    print(get_gear_with_two_part_numbers(content_file_list))