#design tic tac toe on a 3 * 3 board
#a class
# to initialize theboard
# a move function, with the option (row, col, player) representing a move of a player
# at a given row and col,
# #note player 1 move - X, player 2 move - O 

class TicTacToe(object):
    def __init__(self, n):
        """
        brute force
        #create the board
        #getting the cols and rows, initalizing them as 0s
        self.board = [[0 for i in range(n)] for j in range(n)]
        #size of board, ideally 3 by 3
        self.n
        """
        #just keep track of the number of rows and cols, and update
        #same with number of diagonals and anti-diagonals
        self.rows = [ 0 for i in range(n)]
        self.cols = [ 0 for i in range(n)]
        self.diag = 0
        self.antiDiag = 0
        self.n = n
        
    #move function
    def move(self, row, col, player):
        """
        brute force
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
            x
             x
              x
            for d in range(n):
                #not this dimension has the same row and cols
                if matrix[d][d] != player: return False
            return True
        #check the anti -diaogonal
        def checkAntiDiag():
              x
             x
            x
            true anti diagonal
            
            for r in range(n):
                #a anti-diagonal col = n - row  - 1
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
        """
        #optimal
        needed = self.n
        if player == 1:
            self.rows[row]+=1
            #got the all the rows used by a player
            if self.rows[row] == needed: return player
            self.cols[col]+=1
            if self.cols[col] == needed: return player
        #if the row is the col, we increase our diagonall
        if row == col: 
            self.diag+=1
            #visited all used diagonals
            if self.diag == needed: return player
        #check anti diagonal count
        if row+col == self.n -1:
            self.antiDiag+= 1
            if self.antiDiag == needed: return player
        #repeat the process for player 2 but deducting count
        if player == 2:
            self.rows[row]-=1
            if self.rows[row] == -needed: return player
            self.cols[col]-=1
            if self.cols[col] == -needed: return player
            if row == col:
                self.diag -=1
                if self.diag == -needed: return player
            if row+col == self.n -1:
                self.antiDiag -= 1
                if self.antiDiag == -needed: return player
        #if still no winner, return 0
        #this solution uses time and space O(n) instead of brute force O(n^2)
        return 0
        
