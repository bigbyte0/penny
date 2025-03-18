# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

from penny import Penny
import pathlib

def run():
    file_path = input("Please enter a path to an .fc file: ")

    p = Penny()
    path = pathlib.Path(file_path)
    with path.open('r') as file:
        p.read(file.readlines())

    for card in p.shuffled():
        print(card.front, end="")
        _ = input()
        print(card.back, end="")
        _ = input()

    print("Session Complete")

if __name__ == '__main__':
    run()