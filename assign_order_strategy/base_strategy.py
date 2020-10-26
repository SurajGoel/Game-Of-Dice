from assign_order_strategy import assign_strategy


class BaseAssignStrategy(assign_strategy.AssignStrategy):

    def __init__(self):
        super(assign_strategy.AssignStrategy, self).__init__()

    def get_order(self, player_list):
        return player_list
