class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        map = {}
        map[1], map[2], map[3] = 1, 2, 3
        for i in xrange(4, n + 1):
            map[i] = long(map[i - 1] + map[i - 2])
        return map[n]
