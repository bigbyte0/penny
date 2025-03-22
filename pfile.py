import pathlib
from typing import Generator


_PENNY_DIR = "penny"

def get_save_dir() -> pathlib.Path:
    """Returns Penny's file save directory"""
    save_dir = pathlib.Path.home() / _PENNY_DIR
    #if not save_dir.exists():
    return save_dir

def write_file(file_name: str, content: any) -> None:
    """Writes a file to Penny's local save directory"""
    with (get_save_dir() / file_name).open('w') as file:
        file.write(content)

def read_file(file_name: str) -> Generator[str]:
    """Reads a file from Penny's local save directory"""
    with (get_save_dir() / file_name).open('r') as file:
        for line in file:
            yield line