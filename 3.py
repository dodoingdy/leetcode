class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = []
        maxlen = 0
        for i in s:
            for j in range(len(a)):
                if a[j] == i:
                    maxlen = len(a) if maxlen < len(a) else maxlen
                    del a[:j + 1]
                    break
            a.append(i)
        maxlen = len(a) if maxlen < len(a) else maxlen
        return maxlen
