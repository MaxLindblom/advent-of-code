""""
Main script for the day 1 problem
"""

from functools import reduce
from pathlib import Path
from src.files.read import file_to_array
from src.print_results import print_results

CALIBRATIONS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

CALIBRATIONS_REVERSED = {
    "eno": "1",
    "owt": "2",
    "eerht": "3",
    "ruof": "4",
    "evif": "5",
    "xis": "6",
    "neves": "7",
    "thgie": "8",
    "enin": "9",
}


def get_calibration_value_part_one(sequence: str) -> int:
    """
    Returns the calibration value for a single sequence, for the first part
    """
    bools = [x.isdigit() for x in sequence]

    first = sequence[bools.index(True)]
    last = sequence[len(bools) - 1 - bools[::-1].index(True)]

    return int(first + last)


def parse_calibration_sequence(sequence: str, calibration_map: dict) -> str:
    """
    Parses a calibration sequence
    """
    word = ""
    for char in sequence:
        for key, value in calibration_map.items():
            if word.find(key) != -1:
                return value
        if char.isdigit():
            return char
        word += char

    return "0"


def get_calibration_value_part_two(sequence: str) -> int:
    """
    Returns the calibration value for a single sequence, for the second part
    """
    first = parse_calibration_sequence(sequence, CALIBRATIONS)
    last = parse_calibration_sequence(sequence[::-1], CALIBRATIONS_REVERSED)

    return int(first + last)


def main():
    """
    Runs the main script
    """
    sequences = file_to_array(Path(__file__).with_name("input.txt"))

    first_result = reduce(
        lambda x, y: x + get_calibration_value_part_one(y), sequences, 0
    )
    second_result = reduce(
        lambda x, y: x + get_calibration_value_part_two(y), sequences, 0
    )

    print_results(first_result, second_result)


if __name__ == "__main__":
    main()
