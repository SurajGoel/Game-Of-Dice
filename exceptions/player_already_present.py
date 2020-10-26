PLAYER_ALREAD_PRESENT = "Error: Player already present"

class PlayerAlreadyPresent(Exception):

    def __init__(self):
        super(Exception, self).__init__()
        print(PLAYER_ALREAD_PRESENT)
