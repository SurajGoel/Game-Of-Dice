from exceptions import player_already_present
from exceptions import player_not_found


class PlayerManager:

    def __init__(self):
        self.player_map = {}
        pass

    def add_player(self, player):
        if player.get_name() in self.player_map:
            raise player_already_present.PlayerAlreadyPresent()
        self.player_map[player.get_name()] = player

    def get_all_players_by_id(self):
        return list(self.player_map.keys())

    def get_player_by_id(self,id):
        if id in self.player_map:
            return self.player_map[id]

        raise player_not_found.PlayerNotFound()
