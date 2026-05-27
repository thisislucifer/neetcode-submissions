class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        if not board :
            return True

        row_set = [set() for i in range(9)]
        col_set = [set() for i in range(9)]
        box_set = [set() for i in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                box_index = ( r // 3 ) * ( 3 ) + ( c // 3 ) 
                if val != ".":
                    if (val in row_set[r]) or (val in col_set[c]) or (val in box_set[box_index]) :
                        return False
                    else :
                        row_set[r].add(val)
                        col_set[c].add(val)
                        box_set[box_index].add(val)
        return True
        