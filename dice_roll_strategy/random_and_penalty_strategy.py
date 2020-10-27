from dice_roll_strategy import roll_dice_strategy
from random import randrange
from ScreenPrinter import ScreenPrinter


class RandomAndPenaltyStrategy(roll_dice_strategy.RollDiceStrategy):

    def __init__(self):
        super(roll_dice_strategy.RollDiceStrategy, self).__init__()
        self.last_dice_roll = {}


    def get_dice_roll(self, player_id):

        self.__get_dice_roll_input()

        roll = randrange(1,7)
        result_roll = roll

        if roll == 1 and player_id in self.last_dice_roll and self.last_dice_roll[player_id] == 1:
            ScreenPrinter.penalise()
            return 0

        while roll == 6:
            ScreenPrinter.roll_again()
            self.__get_dice_roll_input()
            roll = randrange(1,7)
            result_roll += roll

        ScreenPrinter.you_rolled(roll)

        self.last_dice_roll[player_id] = result_roll
        return result_roll

    def __get_dice_roll_input(self):
        val = 0
        while True:
            val = input("Press 'r' to roll: ")
            if val == "r":
                break
