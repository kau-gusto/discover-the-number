from random import random
from game.reutils import title
from utils.text import clear


class DiscoverNumber:
    def __init__(self, high_number: int) -> None:
        assert high_number >= 2, "the largest number must be greater than 2"
        self.high_number = high_number
        self.small_number = 0
        self.final_number = int(random() * (high_number - 1)) + 1
        self.attempts = 0

    def _discover_number(self):
        title()

        print(f"input one number ({self.small_number}-{self.high_number}):")

        choose = input("")
        assert choose.isnumeric(), "choose a valid number"

        result = int(choose)
        assert self.small_number < result and result < self.high_number, f"choose a number between {self.small_number} and {self.high_number}"

        self.attempts += 1
        if (self.final_number > result):
            self.small_number = result
            assert False, "the final number is greater than " + str(result)
        elif (self.final_number < result):
            self.high_number = result
            assert False, "the final number is less than " + str(result)

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
