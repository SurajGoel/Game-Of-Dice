import sys

from Player import Player
from GameOfDice import GameOfDice
from GameState import GameState
from PlayerManager import PlayerManager
from assign_order_strategy import assign_strategy_factory
from dice_roll_strategy import dice_roll_strategy_factory


args = sys.argv

number_of_players = int(args[1])
winning_score = int(args[2])

player_manager = PlayerManager()
game_state = GameState(winning_score)
assign_strategy_factory = assign_strategy_factory.AssignOrderStrategyFactory()
assign_strategy = assign_strategy_factory.get_assign_order_strategy("random")
dice_roll_strategy_factory = dice_roll_strategy_factory.DiceRollStrategyFactory()
dice_roll_strategy = dice_roll_strategy_factory.get_dice_roll_strategy("random")

game = GameOfDice(number_of_players, player_manager, assign_strategy, dice_roll_strategy, game_state)


for i in range(1, number_of_players+1):
    p = Player(str(i))
    game.add_player(p)

status = game.start_game()

if status:
    while not game.game_completed():
        game.fire_next_simulation()
        game.show_score_board()
