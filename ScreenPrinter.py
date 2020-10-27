class ScreenPrinter:

    def __init__(self):
        pass

    @classmethod
    def starting_game(cls):
        print("Starting Game...")

    @classmethod
    def need_at_least_one_player(cls):
        print("Need at least one player to start the game. Exiting...")

    @classmethod
    def print_leader_board(cls,leader_board):
        pass

    @classmethod
    def print_player_turn(cls, player):
        print("")
        print("It's your turn Player-%s " % player.get_name())

    @classmethod
    def game_finished(cls):
        print("Game is already completed !!")

    @classmethod
    def game_completed(cls):
        print("Game is completed !")

    @classmethod
    def roll_again(cls):
        print("It's a 6, Roll again !")

    @classmethod
    def you_rolled(cls, roll):
        print("You rolled: %s " % roll)

    @classmethod
    def penalise(cls):
        print("You rolled 1 again, you will be penalised !")

    @classmethod
    def print_completed_player_rank(cls,player_id, rank):
        print("Player-%s you have completed the game. Your rank is %s " % (player_id,rank))

    @classmethod
    def print_player_score(cls, player_id, score):
        print("Player-%s your current score is %s" % (player_id, score))

    @classmethod
    def print_playing_order(cls, player_order):
        print("Playing order is: ")
        for i in player_order:
            print("Player-%s" % i)
