from exceptions import player_limit_reached
from ScreenPrinter import ScreenPrinter

MAX_PLAYER_LIMIT = 6


class GameOfDice:

    def __init__(self,
                 player_limit,
                 player_manager,
                 assign_strategy,
                 dice_roll_strategy,
                 game_state):

        self.player_limit = player_limit
        self.player_manager = player_manager
        self.game_state = game_state
        self.player_count = 0
        self.assign_strategy = assign_strategy
        self.dice_roll_strategy = dice_roll_strategy
        self.current_player = None

    def add_player(self, player):
        if self.player_count == self.player_limit:
            raise player_limit_reached.PlayerLimitException()
        self.player_manager.add_player(player)

    """
    Apply a playing order for all the added players and start the game.
    This will take O(n) time.
    """
    def start_game(self):

        if len(self.player_manager.get_all_players_by_id()) == 1:
            ScreenPrinter.need_at_least_one_player()
            return False

        ScreenPrinter.starting_game()

        player_order = self.assign_strategy.get_order(self.player_manager.get_all_players_by_id())
        ScreenPrinter.print_playing_order(player_order)

        self.game_state.initialize_game_state(player_order)

        return True

    """
    Fire next loop for the game
    """
    def fire_next_simulation(self):
        ScreenPrinter.print_player_turn(self.player_manager.get_player_by_id(self.game_state.get_current_player_id()))

        if self.game_state.game_completed():
            ScreenPrinter.game_finished()
            return

        dice_number = self.roll_dice()
        self.game_state.update_game_state(dice_number)

        if self.game_state.game_completed():
            ScreenPrinter.game_completed()

    def roll_dice(self):
        get_dice_role = self.dice_roll_strategy.get_dice_roll(self.game_state.get_current_player_id())
        return get_dice_role

    def show_score_board(self):
        print(self.game_state.score_board)

    def game_completed(self):
        return self.game_state.game_completed()
