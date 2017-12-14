class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        maxleft = 0
        maxright = len(height) - 1
        left, right = 0, len(height) - 1
        while left < right:
            if height[left] < height[right]:
                if height[left] < height[maxleft]:
                    water += height[maxleft] - height[left]
                else:
                    maxleft = left
                left += 1
            else:
                if height[right] < height[maxright]:
                    water += height[maxright] - height[right]
                else:
                    maxright = right
                right -= 1
        return water
