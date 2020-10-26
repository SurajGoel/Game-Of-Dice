from assign_order_strategy import assign_strategy
from random import randrange

class RandomAssignStrategy(assign_strategy.AssignStrategy):

    def __init__(self):
        super(assign_strategy.AssignStrategy,self).__init__()

    def get_order(self, player_list):
        for idx in range(0,len(player_list)):
            swap_index = randrange(0,len(player_list)-1)
            temp = player_list[idx]
            player_list[idx] = player_list[swap_index]
            player_list[swap_index] = temp

        return player_list
