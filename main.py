# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

from penny import Penny
import pathlib
import sys
import pfile

def find_arg(arg_name: str) -> any:
    pass

def find_bool_arg(arg_names: tuple[str, str]) -> bool:
    for arg in sys.argv:
        if arg[2:] in arg_names:
            return True
    return False

FLAG_USE_DEFAULT_CONFIG = ('d', 'default')

def run():
    p = Penny()

    if not find_bool_arg(FLAG_USE_DEFAULT_CONFIG):
        # Try reading the config file
        p.config(list(pfile.read_file(".pennyrc")))

    # Read the input file
    with pathlib.Path(sys.argv[1]).open('r') as file:
        p.read(file.readlines())
    print()

    for card in p.shuffled():
        print(card.front, end="")
        _ = input()
        print(card.back, end="")
        _ = input()
        print()

    print("*** Session Complete ***")

if __name__ == '__main__':
    run()