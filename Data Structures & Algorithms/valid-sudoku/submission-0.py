from itertools import product
from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        # combine with or to get new value and check xor 
        # if xor fails, discard
        for i, j in product(range(9), range(9)):
            el = board[i][j]
            if el=='.':
                continue
            if el in rows[i]:
                return False
            else:
                rows[i].add(el)
            if el in cols[j]:
                return False
            else:
                cols[j].add(el)
            box_num = self.get_box_num(i,j)

            if el in boxes[box_num]:
                return False
            else:
                boxes[box_num].add(el)
        return True

    @staticmethod
    def get_box_num(i,j):
        col_div = j//3
        row_div = i//3
        return 3 * row_div + col_div                