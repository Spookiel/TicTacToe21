from abc import ABC, abstractmethod
from Game import Game
class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        pass

    def run(self):
        pass

class Terminal(Ui):
    def __init__(self):
        self.__game = Game()

    def run(self):
        
        while not self.__game.winner:
            row = int(input("Enter row number: (0,2)"))
            col = int(input("Enter col number: (0,2)"))
            self.__game.play(row, col)