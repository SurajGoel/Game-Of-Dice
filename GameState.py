from ScreenPrinter import ScreenPrinter


class GameState:

    def __init__(self, winning_score):
        self.winning_score = winning_score
        self.playing_order = None
        self.players_count = None
        self.current_player = None
        self.current_player_id = None
        self.prev_player = None
        self.score_board = {}
        self.completed_players = set()
        self.game_finished = False
        self.rank_to_assign = 1

    def initialize_game_state(self, playing_order):

        node = None
        temp = None
        for player_id in playing_order:
            self.score_board[player_id] = {"score": 0, "rank": None}
            new_node = Node(player_id)
            if node is None:
                node = new_node
                temp = node
            else:
                temp.next = new_node
                temp = temp.next

        temp.next = node
        self.playing_order = node
        self.players_count = len(playing_order)
        self.current_player = self.playing_order

    """
    Update game state function.
    Will take points as an input and will update the Game State in O(1) Time complexity
    """
    def update_game_state(self, points):

        if self.game_completed():
            ScreenPrinter.game_completed()
            return

        if self.prev_player is None:
            self.prev_player = self.current_player

        current_player_score = self.score_board[self.current_player.id()]["score"]
        new_score = current_player_score + points
        self.score_board[self.get_current_player_id()]["score"] = new_score
        ScreenPrinter.print_player_score(self.get_current_player_id(), new_score)

        if new_score >= self.winning_score:
            self.__move_current_player_to_completed()
        else:
            self.__increment_player()

    def get_score_board(self):
        return self.score_board

    def game_completed(self):
        return self.game_finished

    def get_current_player(self):
        return self.current_player

    def get_current_player_id(self):
        return self.get_current_player().id()

    """
    If the score that was added to current player pass the winning score, the current player will be moved to Completed state.
    This will remove the completed player from the Linked list representing the players playing
    This will be executed in O(1) Time complexity.
    """
    def __move_current_player_to_completed(self):

        self.completed_players.add(self.get_current_player_id())
        self.__mark_current_player_rank(self.rank_to_assign)
        self.rank_to_assign += 1
        self.prev_player.next = self.current_player.next
        self.current_player = self.current_player.next

        if self.rank_to_assign == self.players_count:
            self.__mark_current_player_rank(self.rank_to_assign)
            self.__mark_game_completed()

    """
    Increment the current player that is playing after a turn is done
    """
    def __increment_player(self):
        self.prev_player = self.current_player
        self.current_player = self.current_player.next

    def __mark_game_completed(self):
        self.game_finished = True

    def __mark_current_player_rank(self, rank):
        self.score_board[self.get_current_player_id()]["rank"] = rank
        ScreenPrinter.print_completed_player_rank(self.get_current_player_id(), rank)

"""
The current players that are playing is represented as a Linked List.
This is done to achieve an O(1) Time complexity for a single game state update.
It's a circular Linked List
For ex:
 if the playing order is: 4,5,3,1,2
 4 -> 5 -> 3 -> 1 -> 2 -> 4 .....
"""
class Node:
    def __init__(self, player_id):
        self.player_id = player_id
        self.next = None

    def id(self):
        return self.player_id
