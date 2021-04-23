from Game import Game
from abc import ABC, abstractmethod
from tkinter import *

from itertools import product
class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        root = Tk()
        root.title("Tic Tac Toe")
        frame = Frame(root)
        frame.pack()
        
        Button(frame, text="Show Help", command=self._help_callback).pack(fill=X)
        Button(frame, text="Play", command=self._play_callback).pack(fill=X)
        Button(frame, text="Quit", command=self._quit_callback).pack(fill=X)
        
        
        
        self.__root = root
    def run(self):
        self.__root.mainloop()
        
    
    def _help_callback(self):
        pass
    
    def _play_callback(self):
        self.__game = Game()
        game_win = Toplevel(self.__root)
        game_win.title("Game")
        frame = Frame(game_win)
        frame.grid(row=0, column=0)
        
        Button(game_win, text="Dismiss", command=game_win.destroy).grid(row=1, column=0)
        
        self.__buttons = [[None]*3 for i in range(3)]
        
        for row, col in product(range(3), range(3)):
            b = StringVar()
            b.set(self.__game.at(row+1, col+1))
            
            cmd = lambda r=row, c=col: self.__play_and_refresh(r,c)
            
            Button(frame, textvariable=b, command=cmd).grid(row=row, column=col)
            self.__buttons[row][col] = b
            
        
    def _quit_callback(self):
        self.__root.quit()
    
    def __play_and_refresh(self, row, col):
        self.__game.play(row+1, col+1)
        
        for row, col in product(range(3), range(3)):
            text = self.__game.at(row+1, col+1)
            self.__buttons[row][col].set(text)
            
class Terminal(Ui):
    def __init__(self):
        self._game = Game()

    def run(self):
        while not self._game.winner:
            print(self._game)
            
            while True:
                try:
                    row = int(input("Which row? "))
                    col = int(input("Which column? "))
                    break
                except ValueError:
                    print("Invalid input, try again!")
            if 1 <= row <= 3 and 1 <= col <= 3:
                if self._game.squares_free() > 0:
                    self._game.play(row,col)
                else:
                    print("No squares free, it is a draw")
                    self._game.winner = "DRAW"
                    break

        print(self._game)
        w = self._game.winner
        print(f"The winner was {w}")
