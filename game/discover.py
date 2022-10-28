from random import random
from game.reutils import title
from utils.text import Colors, clear


class DiscoverNumber:
    def __init__(self, high_number: int) -> None:
        assert high_number >= 2, "the largest number must be greater than 2"
        self.high_number = high_number
        self.small_number = 0
        self.final_number = int(random() * (high_number - 1)) + 1
        self.attempts = 0

    def _discover_number(self):
        title()

        choose = input(
            f"enter a number {Colors.BOLD + Colors.ITALIC}({self.small_number}-{self.high_number}){Colors.CLEAR}: \n")

        assert choose.isnumeric(), Colors.RED + "choose a valid number" + Colors.CLEAR

        result = int(choose)
        assert self.small_number < result and result < self.high_number, Colors.YELLOW + \
            f"choose a number between {Colors.UNDERLINE}{self.small_number}{Colors.CLEAR + Colors.YELLOW} and {Colors.UNDERLINE}{self.high_number}" + Colors.CLEAR

        self.attempts += 1
        if (self.final_number > result):
            self.small_number = result
            assert False, Colors.GREEN + "the final number is greater than " + \
                str(result) + Colors.CLEAR
        elif (self.final_number < result):
            self.high_number = result
            assert False, Colors.GREEN + "the final number is less than " + \
                str(result) + Colors.CLEAR

    def run(self):
        clear()
        while True:
            try:
                return self._discover_number()
            except KeyboardInterrupt as ex:
                raise ex
            except BaseException as ex:
                clear()
                print(ex)
