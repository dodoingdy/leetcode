class Solution(object):
    results = []
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.results = []
        candidates.sort(reverse = True)
        self.dfs(candidates, target, [])
        return self.results
                
    def dfs(self, candidates, target, result):
        import copy
        if target == 0:
            self.results.append(result)
            return
        for i, n in enumerate(candidates):
            if n > target:
                continue
            else:
                self.dfs(candidates[i:], (target - n), copy.copy(result + [n]))
        return
