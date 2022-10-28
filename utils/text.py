import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_all_terminal(text: str, fill_char: str):
    print(text.center(os.get_terminal_size().columns, fill_char))


class Colors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CLEAR = '\033[0m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
