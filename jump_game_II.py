class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        left, right, max_right, step = 1, 0 + nums[0], 0 + nums[0], 0
        while max_right < len(nums) - 1:
            step += 1
            for i in range(left, right + 1):
                max_right = max(i + nums[i], max_right)
            left = right + 1
            right = max_right
        return step + 1
