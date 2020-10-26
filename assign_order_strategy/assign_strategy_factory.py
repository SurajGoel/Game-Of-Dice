from assign_order_strategy import base_strategy
from assign_order_strategy import random_assign_strategy

STRATEGIES = {
    "base": base_strategy.BaseAssignStrategy,
    "random": random_assign_strategy.RandomAssignStrategy
}


class AssignOrderStrategyFactory():

    def get_assign_order_strategy(self, strategy):
        if strategy in STRATEGIES:
            return STRATEGIES[strategy]()

        return STRATEGIES[self.base_strategy()]()

    def base_strategy(self):
        return "base"
