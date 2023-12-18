""""
Main script for the day X problem
"""

from pathlib import Path
from src.files.read import file_to_array
from src.print_results import print_results

def main():
    """
    Runs the main script
    """
    sequences = file_to_array(Path(__file__).with_name('input.txt'))

    first_result = len(sequences)
    second_result = len(sequences)

    print_results(first_result, second_result)

if __name__ == '__main__':
    main()
