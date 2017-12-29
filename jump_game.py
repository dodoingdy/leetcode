class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_right = 0 + nums[0]
        left, right = 0, 0
        while max_right < len(nums) - 1:
            if max_right == right:
                return False
            left, right = right + 1, max_right
            for i in range(left, right + 1):
                max_right = max(max_right, i + nums[i])
        return True
