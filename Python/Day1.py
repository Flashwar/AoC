import re

word_to_digit = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def solution_first_task(lst: list)-> int:

    number_list = []
    for instruction in lst:

        z = [x for x in instruction if x.isdigit()]
        number_list.append(int(z[0] + z[-1]))

    #print([ letter[line_number * 2 + 0] for line in lst for line_number,letter in enumerate(line) if letter.isdigit()])
    return sum(number_list)

def solution_seccond_task(lst: list)-> int:
    pattern = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))')
    number_list = []
    number_2_list = []
    for instruction in lst:
        matches = pattern.findall(instruction)

        digit_tens, digit_ones = matches[0], matches[-1]

        if not digit_tens.isdigit():
            digit_tens =word_to_digit.get(digit_tens)
        if not digit_ones.isdigit():
            digit_ones = word_to_digit.get(digit_ones)

        number_list.append(int(digit_tens + digit_ones))
        #print(digit_tens + digit_ones)
        number_2_list.append(int(word_to_digit.get(matches[0], matches[0]) + word_to_digit.get(matches[-1], matches[-1])))
    return sum(number_list)


def open_read_file(filename: str):

    with open(filename, "r") as f:
        lines = f.readlines()
    return lines



if __name__ == '__main__':

    content_file_list: list = open_read_file("./input/day1_1.txt")

    print(solution_seccond_task(content_file_list))
