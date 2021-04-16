
class Game:
    
    EMPTY = " "
    P1 = "o"
    P2 = "x"
    def __init__(self):
        self.__board = [[Game.EMPTY*3] for _ in range(3)]
        self.__player = Game.P1
    def __repr__(self):
        pass

    def play(self,row,col):
        self.__board[row][col] = self.__player
        self.__player = Game.P1 if self.__player==Game.P2 else Game.P2
    
    @property
    def winner(self):
        
        #Check the rows
        for i in range(3):
            if len(set(self.__board[i]))==1:
                return self.__board[i][0]
        
                

if __name__ == "__main__":
    pass
