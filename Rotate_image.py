class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        glen = length - 1
        for i in range(length/2):
            for j in range(i, glen - i):
                matrix[i][j], matrix[j][glen - i], matrix[glen - j][i], matrix[glen - i][glen - j] = \
                matrix[glen - j][i], matrix[i][j], matrix[glen - i][glen - j], matrix[j][glen - i]
