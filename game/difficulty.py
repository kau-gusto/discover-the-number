from game.reutils import title
from utils.text import clear


class ChooseDifficulty:

    def __init__(self) -> None:
        self.choose: int = None

    def _choose_difficulty(self):
        title()

        print("choose the difficulty:")
        print("(1) 1-10")
        print("(2) 1-100")
        print("(3) 1-1000\n")

        choose = input("")
        assert choose.isnumeric(), "choose a valid number"

        result = int(choose)
        assert result >= 1 and result <= 3, "choose a number between 1 and 3"

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