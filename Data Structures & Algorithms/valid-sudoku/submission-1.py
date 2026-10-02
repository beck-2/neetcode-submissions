class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #only check whether the board is CURRENTLY in a valid state
        #use a hash map and check for collisions? O(n^2) time and O(n^2) space
        #construct sets do see if it's valid? i.e. 
        #{{1,2},{4},{9,8}} would ba a box
        from collections import defaultdict
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set) # key is r //3, c //3
        for r in range(9): #can hardcode because board is fixed size
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True

    
        

