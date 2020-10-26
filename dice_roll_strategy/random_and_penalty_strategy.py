from dice_roll_strategy import roll_dice_strategy
from random import randrange
from ScreenPrinter import ScreenPrinter


class RandomAndPenaltyStrategy(roll_dice_strategy.RollDiceStrategy):

    def __init__(self):
        super(roll_dice_strategy.RollDiceStrategy, self).__init__()


    def get_dice_roll(self):

        self.__get_dice_roll_input()

        roll = randrange(1,7)
        if roll == 6:
            ScreenPrinter.roll_again()
        else:
            ScreenPrinter.you_rolled(roll)
            return roll

        self.__get_dice_roll_input()

        next_roll = randrange(1,7)
        if next_roll == 6:
            ScreenPrinter.penalise()
            return 0
        else:
            ScreenPrinter.you_rolled(next_roll)

        return roll + next_roll

    def __get_dice_roll_input(self):
        val = 0
        while True:
            val = input("Press 'r' to roll: ")
            if val == "r":
                break
