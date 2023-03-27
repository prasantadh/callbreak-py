class GameIsNotOnError(Exception):
    def __init__(self) -> None:
        self.message = "No running game! Request a /new one!"
        super().__init__(self.message)

class TooManyPlayersError(Exception):
    def __init__(self) -> None:
        self.message = "No space for additional players! Sorry!"
        super().__init__(self.message) 
