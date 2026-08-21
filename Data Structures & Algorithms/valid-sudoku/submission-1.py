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
        for boxRow in range(0, 9, 3):
            for boxCol in range(0, 9, 3):
                squareHash = {}
                for i in range(boxRow, boxRow + 3):
                    for j in range(boxCol, boxCol + 3):
                        val = board[i][j]
                        if val.isalnum():
                            if val in squareHash:
                                return False
                            squareHash[val] = True
    
        return True