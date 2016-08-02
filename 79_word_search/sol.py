class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(curr,x,y):
            if curr==len(word):
                return True
            if x>0 and board[x-1][y]==word[curr]:
                board[x-1][y],temp='#',board[x-1][y]
                if dfs(curr+1,x-1,y):
                    return True
                board[x-1][y]=temp
            if x<len(board)-1 and board[x+1][y]==word[curr]:
                board[x+1][y],temp='#',board[x+1][y]
                if dfs(curr+1,x+1,y):
                    return True
                board[x+1][y]=temp
            if y>0 and board[x][y-1]==word[curr]:
                board[x][y-1],temp='#',board[x][y-1]
                if dfs(curr+1,x,y-1):
                    return True
                board[x][y-1]=temp
            if y<len(board[0])-1 and board[x][y+1]==word[curr]:
                board[x][y+1],temp='#',board[x][y+1]
                if dfs(curr+1,x,y+1):
                    return True
                board[x][y+1]=temp
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    board[i][j],temp='#',board[i][j]
                    if dfs(1,i,j):
                        return True
                    board[i][j]=temp
        return False


class Solution_self(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == word[0]:
                    board[i][j], tmp = '#', board[i][j]
                    if self.dfs(word[1:], board, i, j):
                        return True
                    board[i][j] = tmp
        return False

    def dfs(self, word, board, i, j):
        if len(word) == 0:
            return True

        if i > 0 and board[i - 1][j] == word[0]:
            board[i - 1][j], tmp = '#', board[i - 1][j]
            if self.dfs(word[1:], board, i - 1, j):
                return True
            board[i - 1][j] = tmp

        if i < len(board) - 1 and board[i + 1][j] == word[0]:
            board[i + 1][j], tmp = '#', board[i + 1][j]
            if self.dfs(word[1:], board, i + 1, j):
                return True
            board[i + 1][j] = tmp

        if j > 0 and board[i][j - 1] == word[0]:
            board[i][j - 1], tmp = '#', board[i][j - 1]
            if self.dfs(word[1:], board, i, j - 1):
                return True
            board[i][j - 1] = tmp

        if j < len(board[0]) - 1 and board[i][j + 1] == word[0]:
            board[i][j + 1], tmp = '#', board[i][j + 1]
            if self.dfs(word[1:], board, i, j + 1):
                return True
            board[i][j + 1] = tmp

        return False

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
sol = Solution_self()
print sol.exist(board, 'ABCB')
