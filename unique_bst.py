class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        results = [1, 1, 2, 5]
        for i in range(4, n + 1):
            left = 0
            right = i - 1
            sum = 0
            while left <= right:
                if left == right:
                    sum += results[left] * results[right]
                    break
                sum += 2 * results[left] * results[right]
                left = left + 1
                right = right - 1
            results.append(sum)
        return results[n]
