class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = {}
        for i in nums:
            m[i] = 1
        i = 1
        while i:
            if i not in m:
                return i
            i += 1
