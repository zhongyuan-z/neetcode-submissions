class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hmapr = {row: set() for row in range(len(board[0]))}
        hmapc = {col: set() for col in range(len(board))}
        hmapb = {}
        for i in range(len(board)): 
            for j in range(len(board[0])): 
                if board[i][j] == ".": 
                    continue
                if board[i][j] in hmapr[i]: 
                    return False
                hmapr[i].add(board[i][j])
                if board[i][j] in hmapc[j]: 
                    return False
                hmapc[j].add(board[i][j])
                modi, modj = i//3, j//3
                temp = (modi, modj)
                if temp in hmapb: 
                    if board[i][j] in hmapb[temp]: 
                        return False
                    hmapb[temp].add(board[i][j])
                else: 
                    hmapb[temp] = set(board[i][j])
        return True
                