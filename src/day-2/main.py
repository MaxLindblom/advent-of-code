""""
Main script for the day 2 problem
"""

from functools import reduce
from pathlib import Path
from src.files.read import file_to_array
from src.print_results import print_results

def parse_game(game: str) -> dict:
    """
    Parses a game, returning the maxes for each color
    While regex is probably more appropriate, this should work fine
    """
    (game, rounds) = game.split(':')
    game_id = int(game.split(' ')[1])
    sets = rounds.split(';')

    max_red = max_green = max_blue = 0

    for s in sets:
        number_colors = s.split(',')
        for e in number_colors:
            [value, color] = e.strip().split(' ')
            if color == 'red':
                max_red = max(max_red, int(value))
            elif color == 'green':
                max_green = max(max_green, int(value))
            elif color == 'blue':
                max_blue = max(max_blue, int(value))

    return {
        'id': game_id,
        'max_red': max_red,
        'max_green': max_green,
        'max_blue': max_blue
    }

def get_id_if_valid_game(parsed_game: dict, bag_config: dict) -> int:
    """
    Returns the id of the game if it is valid, otherwise returns 0
    """
    if (
        parsed_game['max_red'] > bag_config['red'] or
        parsed_game['max_green'] > bag_config['green'] or
        parsed_game['max_blue'] > bag_config['blue']
    ):
        return 0
    return parsed_game['id']

def get_power_of_game(parsed_game: dict) -> int:
    """
    Returns the power of the game
    """
    return parsed_game['max_red'] * parsed_game['max_green'] * parsed_game['max_blue']

def main():
    """
    Runs the main script
    """
    games = file_to_array(Path(__file__).with_name('input.txt'))
    bag_config = {'red': 12, 'green': 13, 'blue': 14}

    first_result = reduce(
        lambda x,
        y: x+get_id_if_valid_game(parse_game(y), bag_config),
        games,
        0
    )
    last_result = reduce(lambda x, y: x+get_power_of_game(parse_game(y)), games, 0)

    print_results(first_result, last_result)

if __name__ == '__main__':
    main()
