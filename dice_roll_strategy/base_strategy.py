from dice_roll_strategy import roll_dice_strategy
from random import randrange

class BaseRollStrategy(roll_dice_strategy.RollDiceStrategy):

    def __init__(self):
        super(roll_dice_strategy.RollDiceStrategy, self).__init__()

    def get_dice_roll(self):
        roll = randrange(1,6)
        print("You rolled: %s " % roll)
        return roll
