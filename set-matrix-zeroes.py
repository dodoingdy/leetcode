class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        cols = []
        rows = []
        if not matrix or not matrix[0]:
            return
        for i,m in enumerate(matrix):
            if i in cols:
                continue
            judge = 0
            for j,n in enumerate(m):
                if n == 0:
                    judge = 1
                    if j in rows:
                        continue
                    rows.append(j)
            if judge:
                cols.append(i)
        for i in cols:
            for j in range(len(matrix[0])):
                print j
                matrix[i][j] = 0
        for j in range(len(matrix)):
            for i in rows:
                matrix[j][i] = 0
