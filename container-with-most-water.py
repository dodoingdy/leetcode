class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_v = 0
        while left < right:
            if height[left] < height[right]:
                max_v = max(max_v, height[left] * (right - left))
                pre_left = left
                left += 1
                while height[left] < height[pre_left]:
                    left += 1
            else:
                max_v = max(max_v, height[right] * (right - left))
                pre_right = right
                right -= 1
                while height[right] < height[pre_right]:
                    right -= 1
        return max_v
