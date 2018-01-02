class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import copy
        if not grid or not grid[0]:
            return 0
        mapt = copy.copy(grid)
        for i,p in enumerate(mapt):
            for j,q in enumerate(p):
                if i > 0 and j > 0:
                    mapt[i][j] += min(mapt[i - 1][j], mapt[i][j - 1])
                elif i == 0 and j > 0:
                    mapt[i][j] += mapt[i][j - 1]
                elif j == 0 and i > 0:
                    mapt[i][j] += mapt[i - 1][j]
                else:
                    continue
        return mapt[len(mapt) - 1][len(mapt[0]) - 1]
