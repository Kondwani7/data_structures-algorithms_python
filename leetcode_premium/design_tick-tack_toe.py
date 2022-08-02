#design tic tac toe on a 3 * 3 board
#a class
# to initialize theboard
# a move function, with the option (row, col, player) representing a move of a player
# at a given row and col,
# #note player 1 move - X, player 2 move - O 

class TicTacToe(object):
    def __init__(self, n):
        #create the board
        #getting the cols and rows, initalizing them as 0s
        self.board = [[0 for i in range(n)] for j in range(n)]
        #size of board, ideally 3 by 3
        self.n
    #move function
    def move(self, row, col, player):
        #can be move of player 1 or 2
        self.board[row][col] = player
        #initialize our n * n and the matrix board
        n = self.n
        matrix = self.board
        #the key is to check the rows,cols, diagonal and anti-diagonal
        #check if we have a winner, build helper functions to solve this
        def checkRow(r):
            for c in range(n):
                if matrix[r][c] != player: return False
            return True
        #check cols
        def checkCols(c):
            for r in range(n):
                if matrix[r][c] !=player: return False
            return True
        #check diagonally
        def checkDiag():
            """
            x
             x
              x
            """
            for d in range(n):
                #not this dimension has the same row and cols
                if matrix[d][d] != player: return False
            return True
        #check the anti -diaogonal
        def checkAntiDiag():
            """
              x
             x
            x
            true anti diagonal
            """
            for r in range(n):
                if matrix[r][n-r-1] != player: return False
            return True
        #now check all rows
        for r in range(n):
            if checkRow(r): return player
        #check all cols
        for c in range(n):
            if checkCols(c): return player
        #check diagonal and anti diagonals
        if checkDiag(): return player
        if checkAntiDiag: return player
        #if no one wins after these moves return 0, draw
        return 0
