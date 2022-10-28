from game.reutils import title
from utils.text import Colors, clear


class ChooseDifficulty:

    def __init__(self) -> None:
        self.choose: int = 0

    def _choose_difficulty(self):
        title()

        print("choose the difficulty:")
        print(
            f"{Colors.BOLD}({Colors.GREEN}0{Colors.CLEAR}{Colors.BOLD}){Colors.CLEAR} 0-2")
        print(
            f"{Colors.BOLD}({Colors.GREEN}n{Colors.CLEAR}{Colors.BOLD}){Colors.CLEAR} 0-10^n\n")

        choose = input("")
        assert choose.isdecimal(), Colors.RED + "choose a valid number" + Colors.CLEAR

        result = int(choose)
        assert result >= 0, Colors.RED + \
            "choose a number greater than or equal to zero" + Colors.CLEAR

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
