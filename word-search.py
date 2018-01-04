class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word or not board:
            return False
        for i,m in enumerate(board):
            for j,n in enumerate(m):
                if n == word[0]:
                    if self.dfs(board, word, i, j):
                        return True
        return False
        
    def dfs(self, board, word, i, j):
        if not word:
            return True
        if i > len(board) - 1 or i < 0 or j > len(board[0]) - 1 or j < 0:
            return False
        if board[i][j] == word[0]:
            tmp = board[i][j]
            board[i][j] = '#'
            result = self.dfs(board, word[1:], i + 1, j) or self.dfs(board, word[1:], i - 1, j) or self.dfs(board, word[1:], i, j - 1) or self.dfs(board, word[1:], i , j + 1)
            board[i][j] = tmp
            return result
        else:
            return False
