from game.difficulty import ChooseDifficulty
from game.discover import DiscoverNumber
from game.reutils import title
from utils.text import clear

if __name__ == "__main__":
    choose_difficulty = ChooseDifficulty()
    choose_difficulty.run()
    difficulty = choose_difficulty.choose

    high_number = \
        10 if difficulty == 1 else \
        100 if difficulty == 2 else \
        1000 if difficulty == 2 else\
        2
    discover = DiscoverNumber(high_number)
    discover.run()

    clear()
    title()
    print(
        "congratulations, you discover the number " +
        str(discover.final_number) +
        " in " +
        str(discover.attempts) +
        " attempts!!\n")
