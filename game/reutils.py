from utils.text import Colors, print_all_terminal


def title():
    print(Colors.BLUE, end="")
    print_all_terminal(
        Colors.CLEAR + Colors.BOLD + " discover the number " + Colors.CLEAR + Colors.BLUE, "=")
    print(Colors.CLEAR, end="")
