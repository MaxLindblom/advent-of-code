""""
Main script for the day 1 problem
"""

from functools import reduce
from pathlib import Path
from src.files.read import file_to_array

CALIBRATIONS = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

CALIBRATIONS_REVERSED = {
    'eno': '1',
    'owt': '2',
    'eerht': '3',
    'ruof': '4',
    'evif': '5',
    'xis': '6',
    'neves': '7',
    'thgie': '8',
    'enin': '9',
}

def get_calibration_value_part_one(sequence: str) -> int:
    """
    Returns the calibration value for a single sequence, for the first part
    """
    bools = [x.isdigit() for x in sequence]

    first = sequence[bools.index(True)]
    last = sequence[len(bools) - 1 - bools[::-1].index(True)]

    return int(first+last)

def get_calibration_value_part_two(sequence: str) -> int:
    """
    Returns the calibration value for a single sequence, for the second part
    """
    first = '0'
    word = ''
    for char in sequence:
        for key, value in CALIBRATIONS.items():
            if word.find(key) != -1:
                first = value
                break
        if first != '0':
            break
        if char.isdigit():
            first = char
            break
        word += char

    last = '0'
    word = ''
    for char in sequence[::-1]:
        for key, value in CALIBRATIONS_REVERSED.items():
            if word.find(key) != -1:
                last = value
                break
        if last != '0':
            break
        if char.isdigit():
            last = char
            break
        word += char

    return int(first+last)

def main():
    """
    Runs the main script
    """
    sequences = file_to_array(Path(__file__).with_name('input.txt'))

    first_result = reduce(lambda x, y: x+get_calibration_value_part_one(y), sequences, 0)
    print('result from first part:')
    print(first_result)

    second_result = reduce(lambda x, y: x+get_calibration_value_part_two(y), sequences, 0)
    print('result from second part:')
    print(second_result)

if __name__ == '__main__':
    main()
