class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = [0] * len(nums)
        for i, n in enumerate(nums):
            if i == 0:
                temp[i] = max(0, nums[i])
            elif temp[i - 1] + nums[i] < 0:
                temp[i] == 0
            else:
                temp[i] = temp[i - 1] + nums[i]
        result = max(temp)
        if not result:
            return max(nums)
        return result
