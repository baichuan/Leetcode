class Solution(object):

    def exist(self, board, word):

        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        if not word:
            return True;
            
        if board == []:
            return False;

        row = len(board);
        col = len(board[0]);

        for i in range(0, row):
            for j in range(0, col):
                if self.DFS(board, word, i, j, row, col):
                    return True;

        return False;
        
        
    def DFS(self, board, word, i, j, row, col):
        
        if board[i][j] == word[0]:
    
            if not word[1:]:
                return True;

            board[i][j] = " "; # used cell and mark as visited

            # check all adjacent cells
        
            if i + 1 < row and self.DFS(board, word[1:], i + 1, j, row, col):
                return True;

            if i - 1 >= 0 and self.DFS(board, word[1:], i - 1, j, row, col):
                return True;

            if j + 1 < col and self.DFS(board, word[1:], i, j + 1, row, col):
                return True;

            if j - 1 >= 0 and self.DFS(board, word[1:], i, j - 1, row, col):
                return True;

            board[i][j] = word[0]; # update the cell to its original
            return False;

        else:
            return False;
