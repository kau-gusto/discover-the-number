import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_all_terminal(text: str, fill_char: str):
    print(text.center(os.get_terminal_size().columns, fill_char))
