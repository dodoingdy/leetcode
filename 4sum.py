class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        taken = {}
        all_nums = {m:i for i, m in enumerate(nums)}
        result = []
        for i, m in enumerate(nums):
            if m in taken:
                continue
            if m > abs(target):
                break
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if target - m - nums[j] - nums[k] in all_nums and all_nums[target - m - nums[j] - nums[k]] > k:
                        result.append((m, nums[j], nums[k], target - m - nums[j] - nums[k]))
        result = list(set(result))
        return result
