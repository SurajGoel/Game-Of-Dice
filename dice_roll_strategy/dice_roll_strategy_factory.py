import dice_roll_strategy
from dice_roll_strategy import base_strategy
from dice_roll_strategy import random_and_penalty_strategy

STRATEGIES = {
    "base": base_strategy.BaseRollStrategy,
    "random": random_and_penalty_strategy.RandomAndPenaltyStrategy
}


class DiceRollStrategyFactory():

    def get_dice_roll_strategy(self, strategy):
        if strategy in STRATEGIES:
            return STRATEGIES[strategy]()

        return STRATEGIES[self.base_strategy()]()

    def base_strategy(self):
        return "base"
