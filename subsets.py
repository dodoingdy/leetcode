class Solution(object):
    results = set()
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.results = set()
        import copy
        self.results.add(tuple([]))
        self.dfs(nums, [])
        r = list(self.results)
        for i,n in enumerate(r):
            r[i] = list(n)
        return r
            
    def dfs(self, nums, end):
        if not nums:
            return
        for i,m in enumerate(nums):
            self.results.add(tuple(end + [m]))
            self.dfs(nums[i+1:], copy.copy(end + [m]))
