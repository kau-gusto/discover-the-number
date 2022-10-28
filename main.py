from game.difficulty import ChooseDifficulty
from game.discover import DiscoverNumber
from game.reutils import title
from utils.text import clear

if __name__ == "__main__":
    choose_difficulty = ChooseDifficulty()
    choose_difficulty.run()
    difficulty = choose_difficulty.choose

    high_number = 10**difficulty if difficulty > 0 else 2
    print(high_number)
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
