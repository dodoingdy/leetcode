class Solution(object):
    results = []
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.results = []
        candidates.sort()
        self.dfs(candidates, target, [])
        return self.results
        
    def dfs(self, candidates, target, result):
        if target == 0:
            if result not in self.results:
                self.results.append(result)
        for i, n in enumerate(candidates):
            if n > target:
                continue
            else:
                self.dfs(candidates[i + 1:], target - n, result + [n])
