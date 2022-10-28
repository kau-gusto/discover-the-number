from game.reutils import title
from utils.text import clear


class ChooseDifficulty:

    def __init__(self) -> None:
        self.choose: int = 0

    def _choose_difficulty(self):
        title()

        print("choose the difficulty:")
        print("(0) 0-2")
        print("(n) 0-10^n\n")

        choose = input("")
        assert choose.isnumeric(), "choose a valid number"

        result = int(choose)
        assert result >= 0, "choose a number greater than or equal to zero"

        self.choose = result

    def run(self):
        clear()
        while True:
            try:
                return self._choose_difficulty()
            except KeyboardInterrupt as ex:
                raise ex
            except BaseException as ex:
                clear()
                print(ex)
