class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < n:
            m, n = n, m
        sum1 = m
        if n == 1:
            return 1
        former = [1] * m
        gg = [0] * m
        for i in range(1, n - 1):
            tmp = sum1
            sum_t = sum1
            for j in range(1, m):
                tmp -= former[j - 1]
                gg[j] = tmp
                sum1 += gg[j]
            for j, p in enumerate(gg):
                if j == 0:
                    continue
                else:
                    former[j] = p
            former[0] = sum_t
        return sum1
