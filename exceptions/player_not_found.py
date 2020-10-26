PLAYER_NOT_FOUND = "Error: Player not found"

class PlayerNotFound(Exception):

    def __init__(self):
        super(Exception, self).__init__()
        print(PLAYER_NOT_FOUND)
