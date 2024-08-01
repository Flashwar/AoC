import os

def binary_func(data_list: list, data_dict : dict, inserted_data: int, mode:bool):
    low_index = 0
    high_index = len(data_list) - 1


    while low_index <= high_index:
        mid_index = (low_index + high_index) // 2

        if data_list[mid_index] <= inserted_data:
            low_index = mid_index + 1
        else:
            high_index = mid_index - 1

    if mode:
        data_list.insert(low_index, inserted_data)
        return data_list
    else:

        if low_index - 1 < 0 and data_list[low_index] > inserted_data:

            return inserted_data
        elif low_index == len(data_list) and (data_list[low_index-1] + data_dict[data_list[low_index-1]][1]) < inserted_data:
            return inserted_data
        else:
            return data_list[low_index - 1]


class SortedDoubleList:

    def __init__(self):
        self.data = []
        self.data_dict = {}

    def insert(self, data):
        self.data = binary_func(self.data,self.data_dict, data[1], True)
        self.data_dict[data[1]] = (data[0],data[2])


    def get(self, data: int):

        index_data = binary_func(self.data, self.data_dict, data, False)
        start_index = self.data_dict.get(index_data, index_data)
        if index_data == start_index:
            return index_data
        else:
            return (data - index_data) + start_index[0]


def get_puzzle_input(filepath: str) -> list:
    with open(filepath) as f:
        content_list = f.readlines()

    return content_list


def create_mapping(start: int, length: int, puzzle_input: list) -> SortedDoubleList:
    #mapping_dict = {"name": puzzle_input[start].replace("\n", "")}

    struct = SortedDoubleList()

    for i in range(start + 1, start + length):

        elements = [int(x) for x in puzzle_input[i].replace("\n", "").split(" ") if x.isdigit()]

        struct.insert(elements)

        #for ident, index_mapping in enumerate(range(elements[0], elements[0] + elements[2])):
        #   mapping_dict[elements[1] + ident] = index_mapping

    return struct




def part_one(file_puzzle: list):
    chained_mapping_list = []

    seeds = ""
    seeds_length = 0

    while file_puzzle[seeds_length] != "\n":
        seeds += file_puzzle[seeds_length]
        seeds_length += 1

    seeds = [int(x) for x in seeds.replace("seeds: ", "").replace("\n", "").split(" ") if x.isdigit()]

    beginning_line_map = seeds_length + 1
    for line in range(seeds_length + 1, len(file_puzzle)):

        if file_puzzle[line] == "\n" or line == len(file_puzzle) - 1:
            mapping = create_mapping(beginning_line_map, line - beginning_line_map, file_puzzle)
            chained_mapping_list.append(mapping)
            beginning_line_map = line + 1

    return min([chained_mapping_list[6].get(chained_mapping_list[5].get(chained_mapping_list[4].get(chained_mapping_list[3].get(chained_mapping_list[2].get(chained_mapping_list[1].get(chained_mapping_list[0].get(seed))))))) for seed in seeds])

if __name__ == '__main__':
    puzzle_input = get_puzzle_input('./input/Day5_1.txt')
    print(part_one(puzzle_input))

    #print(binary_func([2,7, 24],{7: (80,17), 24:(98,3)}, 29, mode= False))
