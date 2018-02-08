class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        taken = {}
        all_nums = {m:i for i, m in enumerate(nums)}
        for i, m in enumerate(nums):
            if m > 0:
                break
            if m in taken:
                continue
            taken[m] = 1
            for j in range(i + 1, len(nums)):
                if 0 - nums[j] - m in all_nums and all_nums[0 - nums[j] - m] > j:
                    result.append((m, nums[j], nums[all_nums[0 - nums[j] - m]]))
        result = list(set(result))
        for i, m in enumerate(result):
            result[i] = list(m)
        return result
