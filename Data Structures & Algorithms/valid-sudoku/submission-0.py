class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check columns
        for i in range(len(board)):
            columnHash = {}
            for j in range(len(board)):
                if board[i][j].isalnum() and board[i][j] in columnHash.keys():
                    return False
                elif board[i][j].isalnum():
                    columnHash[board[i][j]] = j
        
        # check rows
        for i in range(len(board)):
            rowHash = {}
            for j in range(len(board)):
                if board[j][i].isalnum() and board[j][i] in rowHash.keys():
                    return False
                elif board[j][i].isalnum():
                    rowHash[board[j][i]] = i

        # check square
        for i in range(len(board)):
            if i % 3 == 0:
                squareHash = {}
            j = 0 
            while j < 3:
                if board[i][j].isalnum() and board[i][j] in squareHash.keys():
                    return False
                elif board[i][j].isalnum():
                    squareHash[board[i][j]] = j
                j += 1
        
        return True