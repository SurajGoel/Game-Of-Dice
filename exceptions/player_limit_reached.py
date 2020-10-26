class PlayerLimitException(Exception):

    def __init__(self):
        super(Exception,self).__init__()
        print("Can't add more players")