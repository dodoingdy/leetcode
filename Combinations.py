class Solution(object):
    results = []
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        import copy
        self.results = []
        self.dfs(range(1, n + 1), k, [])
        return self.results
    
    def dfs(self, n, k, end):
        if not k:
            self.results.append(end)
        if not n or len(n) < k:
            return
        for i in n:
            self.dfs(range(i + 1, n[-1] + 1), k - 1, copy.copy(end + [i]))
