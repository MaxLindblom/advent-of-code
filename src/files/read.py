"""
Logic connected to reading files
"""

import locale

def file_to_array(path):
    """
    Reads a file and returns an array of the lines
    """
    with open(path, encoding=locale.getpreferredencoding(False)) as file:
        return file.readlines()
